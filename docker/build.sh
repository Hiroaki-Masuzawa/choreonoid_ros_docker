set -x
SCRIPT_DIR=$(cd $(dirname $0); pwd)

STRING=`groups|grep docker`
SUDO=""
if [ -z "$STRING" ]; then
  SUDO="sudo "
fi

$SUDO docker build -t choreonoid_ros -f $SCRIPT_DIR/Dockerfile $SCRIPT_DIR