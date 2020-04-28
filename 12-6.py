reducible_d = dict()

def words_dictionary():
	d = dict()
	fin = open('words.txt')
	for line in fin:
		d[line.strip()] = None
	return d


def children_dictionary(d):
	children = dict()
	for x in d:
		children[x] = []
		for char_index in range(len(x)):
			missing_a_char = x[0: char_index] + x[char_index + 1:]
			if missing_a_char in d:
				children[x].append(missing_a_char)

	remove_empty_children(children)
	return children

def remove_empty_children(d):
	empty_child_list = []
	for x in d:
		if len(d[x]) == 0:
			empty_child_list.append(x)
	for y in empty_child_list:
		del d[y]


def reducible(word, children_dictionary):
	children = children_dictionary.get(word, [])
	if len(children) > 0:
		if word in reducible_d:
			return True
		if len(word) == 1:
			reducible_d[word] = True	
			return True
		for x in children:
			return reducible(x, children_dictionary)
	else:
		return False

def reducible_print(word, children_dictionary):
	children = children_dictionary.get(word, [])
	print(word)
	if len(word) == 1:
		return True
	if len(children) > 0:
		for x in children:
			return reducible_print(x, children_dictionary)
	else:
		return False

if __name__ == '__main__':
	cd = children_dictionary(words_dictionary())
	wl = list(cd.keys())
	reduc_w = list()
	print(reducible_print('degradations', cd))
	# for x in wl:
	# 	reduc_w.append((len(x),x))

	# reduc_w.sort()
	# print(reduc_w)
	# reduc_l = []
	# for x in wl:
	# 	if reducible_print(x, cd):
	# 		reduc_l.append((len(x), x))
	# reduc_l.sort()
	# print()
	# for y in reduc_l:
	# 	print(cd.get(y[1], None))
