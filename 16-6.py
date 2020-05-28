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

	def mult_time(self, mutliplier):
		given_time = (self.hour * 60 ** 2) + self.minute * 60 + self.second
		mult_time = given_time * mutliplier
		ret_time = Time(0, 0, mult_time)
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
	def avg_pace(self, multiplier):
		return self.mult_time(1 / multiplier)

if __name__ == '__main__':
	time_now = Time(1,0,0)
	pace = time_now.avg_pace(5)
	pace.print_time()
	