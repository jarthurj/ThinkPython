def invert_dict(d):
	inverse = dict()
	for key in d:
		val = d[key]
		if val not in inverse:
			inverse[val] = [key]
		else:
			inverse[val].append(key)
	return inverse

def invert_dict2(d):
	inverse = dict()
	for key in d:
		val = d[key]
		inverse.setdefault(val, []).append(key)
	return inverse

def histogram2(s):
	d = dict()
	for c in s:
		d[c] = d.get(c, 0) + 1
	return d

if __name__ == '__main__':
	letters_count = histogram2('dickbuttassfuckshit')
	count = invert_dict2(letters_count)
	print(count)