def print_hist(d):
	l = list(d.keys())
	l.sort()
	print(l)

def histogram2(s):
	d = dict()
	for c in s:
		d[c] = d.get(c, 0) + 1
	return d


if __name__ == '__main__':
	word_dict = histogram2('buttsassdicksfuck')
	print_hist(word_dict)
