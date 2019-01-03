## ROS Extension for Scratch 3

### This Project has been moved to https://github.com/Affonso-Gui/scratch-vm/tree/develop/src/extensions/scratch3_ros

**WORK IN PROGRESS**

![scratch3-ros](https://user-images.githubusercontent.com/20625381/46603998-c394a400-cb2f-11e8-82e3-a8a6c39050d0.png)

### Run from browser

Access [https://affonso-gui.github.io/scratch-gui](https://affonso-gui.github.io/scratch-gui).

**MALFUNCTION on ROS connection**

### Run from source

```bash
sudo apt install npm # Tested with versions 6.4.0 and 10.12.0
mkdir Scratch; cd Scratch
git clone https://github.com/Affonso-Gui/scratch-vm.git
git clone https://github.com/Affonso-Gui/scratch-gui.git

cd scratch-vm
npm install
npm link

cd ../scratch-gui
npm install
npm link scratch-vm
npm start
```

Then, access [http://localhost:8601](http://localhost:8601).

### Basic Usage

Basic inverse kinematics sample from `tork_moveit_tutorial` using `MoveGroupCommander` interface is reproduced in Scratch 3 and shown below.

![tork_example](https://user-images.githubusercontent.com/20625381/47195260-183ce800-d396-11e8-8214-4e75eadc73ff.png)

**TODO: Add scratch built-in documentation** 

### Demo Program

This repository have sample programs and launch files for using Scratch 3 ROS extension to control PR2 robot.

To run demos launch `demo.launch` on a terminal and load files places on `examples/` from Scratch 3.

![pr2_cup_demo](https://user-images.githubusercontent.com/20625381/47195265-1bd06f00-d396-11e8-826e-38bcbd187969.png)

**TODO: add turtlesim and turtlebot demos**
