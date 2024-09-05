import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/samuel/Learning_ROS/final_project_ros2_ws/install/turtle_sim_catch_them_all'
