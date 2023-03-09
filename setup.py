#!/usr/bin/env python

from setuptools import setup

# Add your package's dependencies here
install_requires = [
    'numpy',
    'scipy',
    'matplotlib',
    'rospy',
    'geometry_msgs',
    # Add any other dependencies here
]

# Fill in your package's information here
setup(
    name='Jaduu_Bot',
    version='0.0.1',
    packages=['jaduu_Bot'],
    install_requires=install_requires,
    author='Sukarna Jana',
    author_email='sukarnascience@gmail.com',
    description='Still its under development',
    license='MIT',
    keywords='ROS',
    url='https://github.com/SukarnaScience/jaduu_Bot',
)
