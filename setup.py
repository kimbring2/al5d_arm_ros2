from setuptools import setup
import os
from glob import glob

package_name = 'al5d_arm_ros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name) + '/launch/', glob('launch/*launch.[pxy][yma]*')),
        (os.path.join('share', package_name) + '/meshes/', glob('meshes/*.*')),
        (os.path.join('share', package_name) + '/rviz/', glob('rviz/*.*')),
        (os.path.join('share', package_name) +  '/urdf/', glob('urdf/*.*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kimbring2',
    maintainer_email='kimbring2@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'controller = al5d_arm_ros2.al5d_arm_controller:main',
        ],
    },
)
