#	Copyright 2022 Technion Research and Development Foundation Ltd.
#
#	MIT LICENSE
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import rclpy
import rclpy.node
from geometry_msgs.msg import Twist
from collections import deque

class Segment:
	def __init__(self, speed = 0.0, turn_rate = 0.0, duration = 0.0):
		self.speed = speed
		self.turn_rate = turn_rate
		self.duration = duration

class CmdVelPublisher(rclpy.node.Node):
	
	def __init__(self):
		super().__init__('assignment1')

		self.declare_parameters(namespace='', parameters=[('duration', 10.0),('turning_rate', 0.15),('speed', 0.21),('shape', 'custom')])

		self._segment_list = deque([])
		self._segment = Segment(speed = self.get_parameter('speed').get_parameter_value().double_value, 
						  turn_rate = self.get_parameter('turning_rate').get_parameter_value().double_value,
						  duration = self.get_parameter('duration').get_parameter_value().double_value)
		self.set_path()
		self._publisher = self.create_publisher(Twist, 'cmd_vel', 10)
		self._timer = self.create_timer(0.1, self.callback)
		self._segment_timer = self.create_timer(self._segment.duration,  self.next_segment)
		
	def set_path(self):
		shape = self.get_parameter('shape').get_parameter_value().string_value
		if ('circle' == shape):
			self.circle()
		elif ('square' == shape):
			self.square()
		elif ('M' == shape):
			self.M()
		else:
			self.custom()
		
	def callback(self):
		twist = Twist()
		twist.linear.x = self._segment.speed
		twist.angular.z = self._segment.turn_rate
		self._publisher.publish(twist)
		
	def next_segment(self):
		if not(self.destroy_timer(self._segment_timer)):
			raise RuntimeError("Could not destroy timer")
		if (0 < len(self._segment_list)):
			done = False
			self._segment = self._segment_list.popleft()
		else:
			done = True
		if done:
			print("Done.")
			self.stop()
		else:
			self._segment_timer = self.create_timer(self._segment.duration,  self.next_segment)
			
	def stop(self):
		self._segment.speed = 0.0
		self._segment.turn_rate = 0.0
		
	def custom(self):
		print("The past is history, the future - a mystery.")
		raise NotImplementedError
		
	############################################################################
	
	def circle(self):
		print("Moving in a circle")
		# TODO Your code here:
		raise NotImplementedError
		# End of your code
	
	def square(self):
		print("Moving in a square")
		# TODO Your code here:
		raise NotImplementedError
		# End of your code
	
	def M(self):
		# TODO Your code here:
		print("Moving in an M")
		raise NotImplementedError
		# End of your code
		
	############################################################################

def main(args=None):
	# ros2 initialization
	rclpy.init(args=args)
	cmd_vel_publisher = CmdVelPublisher()
	# Do
	try:
		rclpy.spin(cmd_vel_publisher)
	except KeyboardInterrupt:
		# Die
		cmd_vel_publisher.destroy_node()
		rclpy.shutdown()

if __name__ == '__main__':
	main()
