# cnoid_tank お試し用


## How to prepare
```
$ cd choreonoid_ros/cnoid_tank
$ ./build.sh
```

## How to use
```
[Terminal 1]
$ cd choreonoid_ros/cnoid_tank
$ ./run.sh
$ source /root/catkin_ws/devel/setup.bash
$ roslaunch cnoid_tank_bringup choreonoid.launch # これが参考ページと異なるので注意
```

```
[Terminal 2]
$ cd choreonoid_ros/cnoid_tank
$ ./exec.sh
$ source /root/catkin_ws/devel/setup.bash
$ roslaunch cnoid_tank_bringup display.launch
```

```
[Terminal 3]
$ cd choreonoid_ros/cnoid_tank
$ ./exec.sh
$ source /root/catkin_ws/devel/setup.bash
$ rosrun rqt_robot_steering rqt_robot_steering _default_topic:=/Tank/base_controller/cmd_vel
```

## Reference
[ros_control連携版 Tankチュートリアル](https://choreonoid.org/ja/manuals/latest/ros/ros-control/index.html)
[cnoid_tank_pkgs](https://github.com/choreonoid/cnoid_tank_pkgs)