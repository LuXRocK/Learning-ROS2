from setuptools import find_packages
from setuptools import setup

setup(
    name='turtlesim_project_interfaces',
    version='0.0.0',
    packages=find_packages(
        include=('turtlesim_project_interfaces', 'turtlesim_project_interfaces.*')),
)
