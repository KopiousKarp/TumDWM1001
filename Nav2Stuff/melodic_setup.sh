#!/bin/bash
apt install -y ros-melodic-desktop-full
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc
apt install -y \
    python3-catkin-pkg \
    python-nose \
    python-setuptools \
    libgtest-dev \
    build-essential \
    git \
    python-rosdep \
    python-rosinstall \
    python-rosinstall-generator \
    python-wstool \
    build-essential
rosdep init
rosdep update
