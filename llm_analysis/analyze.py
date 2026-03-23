"""
Post-race log analyzer — calls Claude API to review driving behavior.

Usage:
    export ANTHROPIC_API_KEY="sk-ant-..."
    python llm_analysis/analyze.py race_log.csv
    python llm_analysis/analyze.py race_log.csv --model claude-sonnet-4-6

The script expects a CSV produced by llm_analysis/logger.py with columns:
    timestamp, x, y, theta, throttle, steer, brake, num_obstacles, min_obstacle_dist
"""

import argparse
import csv
import sys
from pathlib import Path

import anthropic

# ---------------------------------------------------------------------------
# constants
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """\
You are an expert autonomous driving engineer reviewing race simulation data.

Vehicle info:
- Length 4.69 m, width 1.85 m, wheelbase 2.87 m
- Control interface: throttle ∈ [0, 1], steer ∈ [-1, 1] (negative=left), brake ∈ [0, 1]
- Runs at 50 Hz; follows a pre-defined reference path; must avoid dynamic obstacles

The motion planner is one of: MPC (Model Predictive Control) or Pure Pursuit.

Analyse the race log and provide:
1. Overall performance summary (speed, smoothness, safety)
2. Identified behavioural patterns (acceleration habits, steering tendencies, braking usage)
3. Potential issues (oscillating steering, excessive braking, slow cornering, obstacle near-misses)
4. Concrete optimisation suggestions for the motion planning parameters or logic
5. One or two priority action items the developer should address first
"""

# ---------------------------------------------------------------------------
# data loading & summarisation
# ---------------------------------------------------------------------------

def load_log(path: str) -> list[dict]:
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        return [{k: float(v) for k, v in row.items()} for row in reader]


def build_prompt(records: list[dict]) -> str:
    """Produce a token-efficient text representation of the log."""
    n = len(records)
    if n == 0:
        return "Log is empty."

    duration = records[-1]["timestamp"] - records[0]["timestamp"]

    throttles = [r["throttle"] for r in records]
    steers    = [r["steer"]    for r in records]
    brakes    = [r["brake"]    for r in records]
    dists     = [r["min_obstacle_dist"] for r in records if r["min_obstacle_dist"] >= 0]

    avg_throttle   = sum(throttles) / n
    avg_abs_steer  = sum(abs(s) for s in steers) / n
    brake_steps    = sum(1 for b in brakes if b > 0.5)
    max_steer      = max(abs(s) for s in steers)
    min_obs_dist   = min(dists) if dists else -1

    # Detect oscillation: count consecutive steer sign flips
    flips = sum(
        1 for i in range(1, n)
        if steers[i] * steers[i - 1] < 0 and abs(steers[i] - steers[i - 1]) > 0.1
    )

    # Sample ~100 rows evenly across the run
    step = max(1, n // 100)
    sampled = records[::step]
    rows = "\n".join(
        f"  t={r['timestamp']:6.1f}s  ({r['x']:7.1f},{r['y']:7.1f})  "
        f"θ={r['theta']:+.2f}  thr={r['throttle']:.2f}  "
        f"str={r['steer']:+.3f}  brk={r['brake']:.2f}  "
        f"obs={int(r['num_obstacles'])}  d={r['min_obstacle_dist']:.1f}m"
        for r in sampled
    )

    return f"""\
=== Race Log Summary ===
Duration          : {duration:.1f} s
Total steps (50Hz): {n}
Avg throttle      : {avg_throttle:.3f}
Avg |steer|       : {avg_abs_steer:.3f}
Max |steer|       : {max_steer:.3f}
Brake steps (>0.5): {brake_steps} / {n}  ({brake_steps/n:.1%})
Steer oscillations: {flips}
Min obstacle dist : {min_obs_dist:.1f} m

=== Sampled Trajectory (every {step} steps) ===
{rows}
"""


# ---------------------------------------------------------------------------
# LLM call
# ---------------------------------------------------------------------------

def analyze(log_path: str, model: str) -> None:
    records = load_log(log_path)
    if not records:
        print("Error: log file is empty.", file=sys.stderr)
        sys.exit(1)

    print(f"Loaded {len(records)} records from '{log_path}'")
    prompt = build_prompt(records)

    client = anthropic.Anthropic()

    print(f"\nSending to {model} for analysis...\n")
    print("=" * 70)

    with client.messages.stream(
        model=model,
        max_tokens=4096,
        thinking={"type": "adaptive"},
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": (
                    "Please analyse the following race log and give me detailed "
                    "feedback on the driving behaviour and how to improve it.\n\n"
                    + prompt
                ),
            }
        ],
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)

    final = stream.get_final_message()
    print("\n" + "=" * 70)
    print(
        f"\n[Tokens used — input: {final.usage.input_tokens}, "
        f"output: {final.usage.output_tokens}]"
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Analyse a Grand Prix race log with Claude."
    )
    parser.add_argument("log_file", help="CSV log file produced by logger.py")
    parser.add_argument(
        "--model",
        default="claude-opus-4-6",
        help="Claude model ID (default: claude-opus-4-6)",
    )
    args = parser.parse_args()

    if not Path(args.log_file).exists():
        print(f"Error: file not found — {args.log_file}", file=sys.stderr)
        sys.exit(1)

    analyze(args.log_file, args.model)


if __name__ == "__main__":
    main()
