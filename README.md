# Introduction
ROS2 package to control the [AL5D robot arm of Lynxmotion](https://www.robotshop.com/products/lynxmotion-al5d-4-degrees-freedom-robotic-arm-combo-kit).

# Setting
1. Directly commnication between ROS2 and motor of robot is impossible. You need to upload the [Arduino program](https://drive.google.com/file/d/1dJOSnEAfzrh7GTa5parboIpwfxzVnE51/view?usp=sharing) into the controller board of robot called the [BotBoarduino](https://www.robotshop.com/products/lynxmotion-botboarduino-robot-controller). That board is same as Arduino Duemilanove.

Command protocol is

^b065s135e010w090g120w000$

2. Download this repository under the src folder of your ROS2 workspace.

3. Build the ROS2 package using below command.
```
$ colcon build --packages-select al5d_arm_ros2
```

4. Run the built package using below command.
```
$  ros2 run al5d_arm_ros2 controller
```
5. 
