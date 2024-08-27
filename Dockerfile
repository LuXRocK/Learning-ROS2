FROM osrf/ros:humble-desktop

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y nano python3-pip

RUN pip3 install setuptools==58.2.0

RUN apt-get install -y \
    ros-humble-gazebo-ros-pkgs \
    ros-humble-rviz2 \
    ros-humble-urdf-tutorial \
    && rm -rf /var/lib/apt/lists/*

RUN rosdep update

RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc \
    && echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> ~/.bashrc \
    && echo "source ~/ros2_ws/install/setup.bash" >> ~/.bashrc \
    && echo "source /usr/share/gazebo/setup.bash" >> ~/.bashrc 

RUN /bin/bash -c "source ~/.bashrc"

CMD ["/bin/bash"]
