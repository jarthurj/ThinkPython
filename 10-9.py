def remove_dupes(in_list):
	out_list = list()
	for x in in_list:
		out_list.append(x)
		count = 0
		for y in out_list:
			if x == y:
				count += 1
		if count > 1:
			out_list.pop()
	return out_list
if __name__ == '__main__':
	x = [1, 2, 2, 3, 3, 4, 4, 5, 6]
	print(remove_dupes(x))