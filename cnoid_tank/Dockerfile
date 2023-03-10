From ros:noetic-ros-core

WORKDIR /root/
RUN apt update && apt install -y git python3-catkin-tools python3-rosdep
RUN mkdir -p catkin_ws/src 
RUN cd catkin_ws/src && \
    git clone https://github.com/choreonoid/choreonoid.git && \
    git clone https://github.com/choreonoid/choreonoid_ros.git && \
    git clone https://github.com/choreonoid/choreonoid_ros_samples.git && \
    git clone https://github.com/choreonoid/choreonoid_joy.git && \
    git clone https://github.com/choreonoid/rtf-test-plant.git && \
    git clone https://github.com/choreonoid/cnoid_tank_pkgs.git && \
    bash choreonoid/misc/script/install-requisites-ubuntu-20.04.sh 
RUN cd catkin_ws && \
    rosdep init && \
    rosdep update && \
    rosdep install -i -y -r --from-paths src 
RUN cd catkin_ws && \
    bash -c "source /opt/ros/noetic/setup.bash; catkin config --cmake-args -DBUILD_CHOREONOID_EXECUTABLE=OFF -DCMAKE_BUILD_TYPE=Release ; catkin build"
RUN apt install -y ros-noetic-rqt-robot-steering