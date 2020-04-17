def is_sorted(in_list):
	x = in_list[:]
	x.sort()
	if in_list == x:
		return True
	else:
		return False
def is_sorted2(in_list):
	for x in range(0, len(in_list) - 1):
		if in_list[x + 1] < in_list[x]:
			return False
	return True

if __name__ == '__main__':
	test1 = [1, 2, 3, 4]
	test2 = [1, 2, 9, 5]
	print(is_sorted2(test1))
	print(is_sorted2(test2))