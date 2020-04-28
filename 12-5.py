def anagram_dictionary():
	fin = open('words.txt')
	anas = dict()
	for line in fin:
		word = line.strip()
		w_list = sorted(list(word))
		key = "".join(w_list)
		anas.setdefault(key, []).append(word)
	remove_keys = list()
	for x in anas:
		if len(anas[x]) <= 1:
			remove_keys.append(x)
	for y in remove_keys:
		del[anas[y]]
	return anas

def values_sort(d):
	l = list()
	for x in d.values():
		l.append((len(x), x))
	l.sort()
	ret_l = list()
	for x in l:
		ret_l.append(x[1])
	return ret_l

def metathesis(l):
	for x in range(len(l) - 1):
		for y in range(x + 1, len(l) - 1):
			count = 0
			for z in range(len(l[0])):
				if l[x][z] != l[y][z]:
					count += 1
			if count == 2:
				print(l[x], l[y])
if __name__ == '__main__':
	d = anagram_dictionary()
	l1 = values_sort(d)
	for x in l1:
		metathesis(x)
