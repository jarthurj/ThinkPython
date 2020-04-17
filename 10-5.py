def chop(in_list):
	del in_list[len(in_list) - 1]
	del in_list[0]

if __name__ == '__main__':
	x = [i for i in range(10)]
	chop(x)
	print(x)