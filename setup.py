from setuptools import setup

package_name = 'air'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='David Dovrat',
    maintainer_email='ddovrat@cs.technion.ac.il',
    description='Technion - Computer Science - AI and Robotics',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
			'assignment1 = air.assignment1:main',
        ],
    },
)
