import datetime
import random
def num_day(num):
	if num == 0: return 'Monday'
	if num == 1: return 'Tuesday'
	if num == 2: return 'Wednesday'
	if num == 3: return 'Thursday'
	if num == 4: return 'Friday'
	if num == 5: return 'Saturday'
	if num == 6: return 'Sunday'

def age(b_day):
	today = datetime.date.today()
	years = today.year - b_day.year

	if b_day < today:
		return years
	else:
		return years - 1

def age_double_day(b_day, double_today):

	years = double_today.year - b_day.year
	if b_day < double_today:
		return years
	else:
		return years - 1

def days_in_month(num, year):
	if num == 1: return 31
	if num == 2:
		if year % 4 == 0:
			return 29
		else: 
			return 28
	if num == 3: return 31
	if num == 4: return 30
	if num == 5: return 31
	if num == 6: return 30
	if num == 7: return 31
	if num == 8: return 31
	if num == 9: return 30
	if num == 10: return 31
	if num == 11: return 30
	if num == 12: return 31

def random_b_day():
	year = random.randint(1900, 2000)
	month = random.randint(1, 12)
	day = random.randint(1, days_in_month(month, year))
	return datetime.date(year, month, day)

def next_bday(b_day):
	today = datetime.date.today()
	next_bday_date = datetime.date(today.year + 1, b_day.month, b_day.day)
	return next_bday_date - today
def double_day(bday1, bday2):
	if bday1 < bday2:
		older_days = (bday2 - bday1).days
		counting_day = bday2
	else:
		older_days = (bday1 - bday2).days
		counting_day = bday1
	younger_days = 0

	while True:
		if older_days == younger_days * 2:
			return counting_day
		older_days += 1 
		younger_days += 1
		counting_day += datetime.timedelta(days=1)
		# print(older_days, younger_days, counting_day)

def n_day(bday1, bday2, n):
	if bday1 < bday2:
		older_days = (bday2 - bday1).days
		counting_day = bday2
	else:
		older_days = (bday1 - bday2).days
		counting_day = bday1
	younger_days = 0

	while True:
		if older_days == younger_days * n:
			return counting_day
		older_days += 1 
		younger_days += 1
		counting_day += datetime.timedelta(days=1)
		# print(older_days, younger_days, counting_day)
if __name__ == '__main__':
	#1
	# day_week = num_day(datetime.date.today().weekday())
	# print(datetime.date.today(), day_week)
	#2
	# b_day = input("Input bday MM/DD/YYYY \n")
	# b_day = b_day.split("/")
	# b_day = datetime.date(int(b_day[2]),int(b_day[0]),int(b_day[1]))
	# print('Age:', age(b_day))
	# print("Next Bday:", next_bday(b_day))
	#3
	bday1 = random_b_day()
	bday2 = random_b_day()
	nday = n_day(bday1, bday2, 3)
	# dday = double_day(bday1, bday2)
	# print(bday1)
	# print(bday2)
	# print("Bday1 Age:",age_double_day(bday1, dday), "Bday2 Age:", age_double_day(bday2, dday))
	print(bday1 - nday)
	print(bday2 - nday)