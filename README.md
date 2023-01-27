## rt1a2
Università di Genova/MSc in Robotics Engineering/Research Track 1/2nd Assignment

**********************
**********************
**********************
**********************
**********************
# [UNIGE Università di Genova](https://unige.it/it/) , [MSc in Robotics Engineering](https://courses.unige.it/10635) , [Research_Track_1](https://unige.it/en/off.f/2021/ins/51201.html?codcla=10635) , Second Assignment
### Professor. [Carmine Recchiuto](https://github.com/CarmineD8)
### Autheor : [Rafael Rabbani](https://github.com/Rouphael)

**********************
**********************
**********************

# 1. Introduction
## This package consist of three nodes working along with the package [assignment_2_2022](https://github.com/CarmineD8/assignment_2_2022) that provides an implementation of an action server that moves a robot in the environment by implementing the bug0 algorithm. The three nodes are:
### 1. a_target_publisher : This node implements an action client, allowing the user to set a target (x, y) or to cancel it. The node also publishes the robot position and velocity as a custom message (x,y, vel_x, vel_z) by subscribing to the odometry topic (/odom).
### 2. b_goal_status : This node is a service node that, when called, prints the number of goals that have been reached and and the number of goals that have been cancelled.
### 3. c_robot_subscriber : This node subscribes to the custom message published by the a_target_publisher node and calculates the distance between the robot and the target and the average speed of the robot. the node also prints the distance and the average speed on the terminal.

**********************
**********************
**********************

# 2. Installation

# 2.1 Guide for starter's (Ubuntu22 os installed)
### If you are new to ROS, you can follow the instruction below to install ROS,Gazebo and other dipendencies and create a workspace and use this package. 
### If you have already done so, you can skip to the next section.

## 2.1.1 Preliminarly install gazebo
```bash
    sudo apt-get install -y gazebo libgazebo-dev
```
## 2.1.2 Add the ros repository
```bash
    sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu focal main" > /etc/apt/sources.list.d/ros-latest.list'
```
```bash
    sudo apt install curl gnupg
```
```bash
    curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```
```bash
    sudo apt update
```
## 2.1.3 Install all needed software
```bash
    sudo apt-get install python3-rosinstall-generator python3-vcstools build-essential python3-pip wget
```
```bash
    sudo pip3 install -U rosdep
```
```bash
    sudo pip3 install wstool
```
## 2.1.4 Initialize the ros workspace
```bash
    sudo rosdep init
```
```bash
    rosdep update
```
```bash
    mkdir ~/ros_catkin_ws
``` 
```bash
    cd ~/ros_catkin_ws
```
```bash
    rosinstall_generator desktop_full --rosdistro noetic --deps --tar > noetic-desktop_full.rosinstall
```
```bash
    mkdir ./src
```
```bash
    wstool init src noetic-desktop_full.rosinstall
```
## 2.1.5 Install hddtemp manually and fix the workspace
```bash
    wget http://archive.ubuntu.com/ubuntu/pool/universe/h/hddtemp/hddtemp_0.3-beta15-53_amd64.deb  
```
```bash
    sudo apt install ./hddtemp_0.3-beta15-53_amd64.deb
```
```bash
    rm hddtemp_0.3-beta15-53_amd64.deb
```
```bash
    cd src/diagnostics/diagnostic_common_diagnostics
```
Open the file package.xml and delete line 21
```bash
    gedit package.xml
```
In following folder
```bash
    cd ../../rosconsole/src/rosconsole/impl/
```
Replace rosconsole_log4cxx.cpp with 
https://raw.githubusercontent.com/AchmadFathoni/rosconsole/c9d161a6d946590bf808eb6006430c8c8d8b5cd6/src/rosconsole/impl/rosconsole_log4cxx.cpp

In following folder
```bash
    cd ../../../../roscpp_core/roscpp_serialization/include/ros/
```
Replace serialization.h with

https://raw.githubusercontent.com/ros/roscpp_core/noetic-devel/roscpp_serialization/include/ros/serialization.h

In following folder :
```bash
    cd ../../../../laser_geometry
```
Open CMAkeLists.txt and change line 4 with: set(CMAKE_CXX_STANDARD 17)

In following folder :
```bash
    cd ../laser_filters
```
Open CMAkeLists.txt and change line 4 with: set(CMAKE_CXX_STANDARD 17)

In following folder :
```bash
    cd ../urdf/urdf
```
Open CMAkeLists.txt and change line 25 with: set(CMAKE_CXX_STANDARD 20)

In following folder :
```bash
    cd ../../kdl_parser/kdl_parser
```
Open CMAkeLists.txt and change line 5 with: set(CMAKE_CXX_STANDARD 20)

In following folder :
```bash
    cd ../../rviz
```
Open CMAkeLists.txt and add line 3: set(CMAKE_CXX_STANDARD 17)

In following folder :
```bash
    cd ../rqt_rviz
```
Open CMAkeLists.txt and add line 4: set(CMAKE_CXX_STANDARD 17)

In following folder :
```bash
    cd ../visualization_tutorials/librviz_tutorial
```
Open CMAkeLists.txt and add line 15 with: set(CMAKE_CXX_STANDARD 17)

In following folder :
```bash
    cd ../rviz_plugin_tutorials
```
Open CMAkeLists.txt and add line 8: set(CMAKE_CXX_STANDARD 17)

In following folder :
```bash
    cd ../../perception_pcl/pcl_ros
```
Open CMAkeLists.txt and change line 9 with: set(CMAKE_CXX_STANDARD 17)

In following folder :
```bash
    cd ../../gazebo_ros_pkgs/gazebo_plugins
```
Open CMAkeLists.txt and add line 5: set(CMAKE_CXX_STANDARD 17)

In following folder :
```bash
    cd ../gazebo_ros_control
```
Open CMAkeLists.txt and add line 3: set(CMAKE_CXX_STANDARD 17)

In following folder :
```bash
    cd ../gazebo_ros
```
Open CMAkeLists.txt and add line 3: set(CMAKE_CXX_STANDARD 17)

```bash
    cd ../../..
```
## 2.1.6 Install all the dependencies
```bash
    rosdep install --from-paths ./src --ignore-packages-from-source --rosdistro noetic -y
```
## 2.1.7 Build the workspace
```bash
    ./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_STANDARD=20
```
## 2.1.8 Setup the .basrhc script
```bash
    cd ..
```
Open .bashrc with a text editor and add the following line at the end of the file: 

source ~/ros_catkin_ws/install_isolated/setup.bash
```bash
    source .bashrc
```
You should have now a full desktop ROS installation in your Ubuntu22 OS!

**********************
# 2.2 Guide with ROS and dependencies installed
### Those who already have ROS and dependencies installed can skip the first part of the guide and start from here.

## 2.2.1 Install the package
Go to the src folder of your workspace
```bash
    cd ~/ros_catkin_ws/src
```
Clone the repository [assignment_2_2022](https://github.com/CarmineD8/assignment_2_2022)
in the src folder
```bash
    git clone https://github.com/CarmineD8/assignment_2_2022.git
```
Clone the repository [rt1a2](https://github.com/Rouphael/rt1a2) in the src folder
```bash
    git clone git@github.com:Rouphael/rt1a2.git
```
Go to your workspace root folder
```bash
    cd ~/ros_catkin_ws/
```
Build any packages located in ~/catkin_ws/src.
```bash
    Catkin_make
```
**********************
**********************
**********************
# 3. Running the package
### You can easily run the package by launching the rt1a2.launch file.

Open a terminal and type
```bash
    roslaunch rt1a2 rt1a2.launch
```
### This will do the following:
* Launch assignment1.launch placed in the assignment_2_2022 package
  * Launch sim_w1.launch 
  * Set the parameters for the robot
  * Launch wall_follower
  * Launch go_to_point
  * Launch bug_action_service
* Launch a_target_status
* Launch b_goal_status
* Launch c_bug_action_client

Now you have Gazebo simuulation with a robot and walls, RViz with the robot model and the laser data, and three terminals oppened.

**********************
**********************
**********************
# 4. Oppened terminals
## Terminal A. 
### In this terminal you can choose to set a target point or to cancel it.
If you want to set a target you can enter 1.

# Picture start

Then you will be asked to enter the x and y coordinates of the target point.

# Picture 1


If you want to cancel the target you can enter 2.

# Picture 2

## Terminal B.
### This terminal will show the number of goals reached and the number of goals cancelled when the service goal_status is called.

# Picture start


For calling goal_status service open a terminal and type
```bash
    rosservice call /goal_status
```

# picture data


## Terminal C.
### This terminal will show robot's distance from the target point and the average speed of the robot with an update rate of publish_speed in Hz.

# Picture start

Publish_speed is set to 2Hz by defult in rt1a2.launch file and you can change it by changing the value of publish_speed in rt1a2.launch file.
```bash
    <param name="publish_speed" value=" <custom update rate> "/>
```
or by oppening a terminal and typing
```bash
    rosparam set /publish_speed <custom update rate>
```

**********************
**********************
**********************
# 4. Node description
## 4.1 a_target_status
### This node implements an action client, allowing the user to set a target (x, y) or to cancel it.



### The node also publishes the robot position and velocity as a custom message (x,y, vel_x, vel_z) by relying on the values published on the topic /odom.