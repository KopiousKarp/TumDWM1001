source /opt/ros/noetic/setup.sh
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
cd src
git clone https://github.com/Slamtec/rplidar_ros.git
cd .. && catkin_make


