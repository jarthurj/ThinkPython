def middle(in_list):
	return in_list[1:-1]
def middle2(in_list):
	out_list = list()
	for x in range(1, len(in_list)):
		out_list.append(in_list[x])

	return out_list
if __name__ == '__main__':
	x = [i for i in range(10)]
	print(x)
	print(middle2(x))