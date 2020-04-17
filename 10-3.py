def cumul_add(in_list):
	sum = 0
	out_list = list()
	for x in in_list:
		sum += x
		out_list.append(sum)
	return out_list


if __name__ == '__main__':
	numbers = [1, 2, 3]
	print(cumul_add(numbers))
