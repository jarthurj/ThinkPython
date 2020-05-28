class Time(object):
	seconds_in_hour = 3600
	seconds_in_minute = 60
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

	def increment(self, seconds):
		total_time = (self.hour * 60 ** 2) + self.minute * 60 + self.second
		new_total_time = total_time + seconds
		if new_total_time >= self.seconds_in_hour:
			self.hour = new_total_time // self.seconds_in_hour
			new_total_time %= self.seconds_in_hour
			if new_total_time >= self.seconds_in_minute:
				self.minute = new_total_time // self.seconds_in_minute
				new_total_time %= self.seconds_in_minute
				self.second = new_total_time
			else:
				self.second = new_total_time
		else:
			if new_total_time >= self.seconds_in_minute:
				self.minute = new_total_time // self.seconds_in_minute
				new_total_time %= self.seconds_in_minute
				self.second = new_total_time
			else:
				self.second = new_total_time

	def increment_pure(self, seconds):
		total_time = (self.hour * 60 ** 2) + self.minute * 60 + self.second
		new_total_time = total_time + seconds
		ret_time = Time(0,0,0)
		if new_total_time >= self.seconds_in_hour:
			ret_time.hour = new_total_time // self.seconds_in_hour
			new_total_time %= self.seconds_in_hour
			if new_total_time >= self.seconds_in_minute:
				ret_time.minute = new_total_time // self.seconds_in_minute
				new_total_time %= self.seconds_in_minute
				ret_time.second = new_total_time
			else:
				ret_time.second = new_total_time
		else:
			if new_total_time >= self.seconds_in_minute:
				ret_time.minute = new_total_time // self.seconds_in_minute
				new_total_time %= self.seconds_in_minute
				ret_time.second = new_total_time
			else:
				ret_time.second = new_total_time
		return ret_time
		
if __name__ == '__main__':
	time_now = Time(7,41,56)
	time_later = Time(11,57,42)
	time_now.print_time()
	print("wait 1 hour")
	new_time = time_now.increment_pure(3600)
	new_time.print_time()
	