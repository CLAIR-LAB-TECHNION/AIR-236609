# Assignment 1

To run the assignment from the project's workspace directory:

```console
ros2 run air assignment1 --ros-args --params-file src/params/assignment1.yaml
```

To fulfill the assignment's requirements, create your own parameter files or change the existing *assignment1.yaml* and implement the *circle*, *square*, and *M* functions in the *assignment1.py* script.

## Parameters

|	Parameter	|	Meaning	|	Default Value	|
|	---------	|	------------	|	-----------	|
|	duration	|	the time allotted to perform a segment [s]	|	1.0	|
|	shape	|	one of: {circle, square, M}, defaults to custom.	|	custom	|
|	speed	|	forward speed in [m/s]	|	0.21	|
|	turning_rate	|	turning rate (to the left) in [rad/s]	| 	0.15	|
|	use_sim_time	|	If true, the clients will adhere to the /clock topic instead of wall clock time.	|	false	|

## Dependencies

* rclpy
* geometry_msgs
