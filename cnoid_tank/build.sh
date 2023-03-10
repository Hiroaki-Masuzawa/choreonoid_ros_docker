SCRIPT_DIR=$(cd $(dirname $0); pwd)

STRING=`groups|grep docker`
SUDO=""
if [ -z "$STRING" ]; then
  SUDO="sudo "
fi
set -x
$SUDO docker build -t cnoid_tank -f $SCRIPT_DIR/Dockerfile $SCRIPT_DIR
