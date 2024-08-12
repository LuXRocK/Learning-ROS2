# Learning ROS2
In this repository I will document my learning experience of ROS2. <br> 
https://www.udemy.com/course/ros2-for-beginners/ <br>
This is the udemy course that I'm following in this repo. <br>

## Purpose
I'm learning ROS2 because in my 5th semester of university I'll be a part of a team working on a project, which goal is 
to deliver a 3D mapping drone, using SLAM technology. <br> 
I have created a notes.txt file in which I'll be writing down important information that might turn out to be useful in the
actual project. 

## Run through Docker 
Since ROS2 works on Ubuntu 22.04 in order to run it on a different machine you have to use Docker.<br>
First build the Dockerfile, to do that run: <br>
```bash 
docker build -t ros2 .
```
While in the directory with Dockerfile. <br>
Then start a docker container that will be able to display GUI with this command: <br> 
```bash
docker run -it --rm \
  --net=host \
  --env="DISPLAY" \
  --env="QT_X11_NO_MITSHM=1" \
  --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
  --name ros2 \
  -v /home/Samuel/Learning-ROS2/ros_ws1:/root/ros2_ws \
  ros2
```
After that, in your local bash run: <br>
```bash
xhost +local:docker
```
If everything works fine you should be able to run rqt in the container. <br>
I'm still working on how to get the same result on Mac but there's a lot of troubleshooting there.
