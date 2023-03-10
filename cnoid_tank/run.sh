set -x
SCRIPT_DIR=$(cd $(dirname $0); pwd)

STRING=`groups|grep docker`
SUDO=""
if [ -z "$STRING" ]; then
  SUDO="sudo "
fi

$SUDO docker run --rm -it \
    --env="DISPLAY" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --name cnoid_tank \
    cnoid_tank bash
