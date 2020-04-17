from random import randint

def has_duplicates(in_list):
	y = in_list[:]
	y.sort()
	for i in range(0, len(in_list) - 1):
		if y[i] == y[i + 1]:
			return True
	return False



if __name__ == '__main__':
	true_count = 0
	for x in range(0, 10000):
		x = [randint(1, 365) for x in range(1, 71)]
		if has_duplicates(x):
			true_count += 1
	print(true_count/10000)


