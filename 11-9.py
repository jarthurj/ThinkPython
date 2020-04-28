def has_duplicates(l):
	d = {}
	for x in l:
		if x in d:
			return True
		else:
			d[x] = True
	return False	

if __name__ == '__main__':
	l = list('asssss')
	print(has_duplicates(l))