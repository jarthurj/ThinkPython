def histogram(s):
	d = dict()
	for c in s:
		if c in d:
			d[c] += 1
		else:
			d[c] = 1
	return d

def histogram2(s):
	d = dict()
	for c in s:
		d[c] = d.get(c, 0) + 1
	return d

if __name__ == '__main__':
	print(histogram('asssss'))
	print(histogram2('asssss'))