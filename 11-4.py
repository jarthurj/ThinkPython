def print_hist(d):
	l = list(d.keys())
	l.sort()
	print(l)

def histogram2(s):
	d = dict()
	for c in s:
		d[c] = d.get(c, 0) + 1
	return d

def reverse_lookup(d, v):
	l = list()
	for x in d:
		if d[x] == v:
			l.append(x)
	return l

if __name__ == '__main__':
	word_dict = histogram2("assbuttdickfuckshit")
	print(reverse_lookup(word_dict, 2))


