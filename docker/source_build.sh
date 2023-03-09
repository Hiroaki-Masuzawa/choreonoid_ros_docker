set -x
SCRIPT_DIR=$(cd $(dirname $0); pwd)

STRING=`groups|grep docker`
SUDO=""
if [ -z "$STRING" ]; then
  SUDO="sudo "
fi

$SUDO docker run --rm -it \
    --user=$(id -u $USER):$(id -g $USER) \
    -v /etc/passwd:/etc/passwd:ro -v /etc/group:/etc/group:ro \
    --env="DISPLAY" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    -v $SCRIPT_DIR/../homedir:$HOME -v $SCRIPT_DIR/../catkin_ws:$HOME/catkin_ws \
    -v /tmp:/host/tmp \
    -v $SCRIPT_DIR/..:/workdir \
    -w /workdir \
    --name choreonoid_ros \
    choreonoid_ros bash -c "cd ~/catkin_ws; catkin build"
