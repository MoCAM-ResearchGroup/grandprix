#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/iotsc/grandprix/bridge/src/carla_ackermann_control"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/iotsc/grandprix/bridge/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/iotsc/grandprix/bridge/install/lib/python3/dist-packages:/home/iotsc/grandprix/bridge/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/iotsc/grandprix/bridge/build" \
    "/usr/bin/python3" \
    "/home/iotsc/grandprix/bridge/src/carla_ackermann_control/setup.py" \
     \
    build --build-base "/home/iotsc/grandprix/bridge/build/carla_ackermann_control" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/iotsc/grandprix/bridge/install" --install-scripts="/home/iotsc/grandprix/bridge/install/bin"
