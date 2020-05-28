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

	def is_after(self, other_time):
		s_1 = (self.hour * 60 ** 2) + self.minute * 60 + self.second
		s_2 = (other_time.hour * 60 ** 2) + other_time.minute * 60 + other_time.second
		if s_1 > s_2:
			return True
		elif s_1 < s_2:
			return False
		elif s_1 == s_2:
			return None

if __name__ == '__main__':
	time_now = Time(7,41,56)
	time_later = Time(11,57,42)
	print(time_later.is_after(time_now))
	