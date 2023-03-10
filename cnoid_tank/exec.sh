set -x
STRING=`groups|grep docker`
SUDO=""
if [ -z "$STRING" ]; then
  SUDO="sudo "
fi

$SUDO docker exec -it cnoid_tank bash