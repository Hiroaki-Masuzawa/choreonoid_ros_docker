# choreonoid_ros

## How to prepare
```
$ cd choreonoid_ros
$ ./build.sh
$ ./source_build.sh
```

## How to use
```
[Terminal 1]
$ cd choreonoid_ros
$ ./run.sh
$  roslaunch choreonoid_ros_control_assembler_sample choreonoid.launch 
```

```
[Terminal 2]
$ cd choreonoid_ros
$ ./exec.sh
$ rostopic pub -1 /AssembleRobot/joint_controler/command trajectory_msgs/JointTrajectory "header:
  seq: 0
  stamp:
    secs: 0
    nsecs: 0
  frame_id: ''
joint_names:
- 'LINK_0'
points:
- positions: [0.5]
  velocities: [0]
  accelerations: [0]
  effort: [0]
  time_from_start: {secs: 1, nsecs: 0}" 
```

## Reference
[choreonoid_ros_controlを自分のロボットに適用してみた話](https://qiita.com/FAL19/items/7b4a491e2399aa5cf7c9)
[ros_control連携版 Tankチュートリアル](https://choreonoid.org/ja/manuals/latest/ros/ros-control/index.html)
[cnoid_tank_pkgs](https://github.com/choreonoid/cnoid_tank_pkgs)