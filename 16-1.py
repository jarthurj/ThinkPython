class Time(object):
	hour = 0
	minute = 0
	second = 0
	def __init__(self, hour, minute, second):
		self.hour = hour
		self.minute = minute
		self.second = second

	def print_time(self):
		print('The time is now: %.2d : %.2d : %.2d' % (self.hour, self.minute, self.second))

if __name__ == '__main__':
	time_now = Time(7,41,56)
	time_now.print_time()
	