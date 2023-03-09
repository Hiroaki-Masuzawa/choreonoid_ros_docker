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
$ roslaunch choreonoid_ros_control_sample bringup.launch
```

```
[Terminal 2]
$ cd choreonoid_ros
$ ./exec.sh
$ rostopic pub -1 /simple_leg/Hip_position_controller/command std_msgs/Float64 -- -0.785
```

## Reference
[choreonoid_ros_controlを自分のロボットに適用してみた話](https://qiita.com/FAL19/items/7b4a491e2399aa5cf7c9)
