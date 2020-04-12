def nested_sum(list):
	total = 0
	for x in list:
		for y in x:
			total += y
	return total
if __name__ == '__main__':
	test_list = [[1, 1, 1], [1, 1, 1], [1, 1],[1]]
	print(nested_sum(test_list))