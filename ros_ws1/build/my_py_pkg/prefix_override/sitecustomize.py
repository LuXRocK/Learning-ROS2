import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/samuel/Learning_ROS/ros_ws1/install/my_py_pkg'
