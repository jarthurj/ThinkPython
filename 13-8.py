import string as str
import random
def punctuation_mapping():
	punc = str.punctuation + '”' + '“' + '—'+ '—'+ '‘' + '’' + '”'
	punc_dict = {}
	for x in punc:
		punc_dict[ord(x)] = None
	return punc_dict

def strip_and_lower(word):
	table = punctuation_mapping()
	word.strip()
	trans_word = word.translate(table)
	ret_word = trans_word.translate(table)
	return ret_word.strip().lower()

def words_list(filename):
	ret_list = list()
	fin = open(filename)
	for line in fin:
		line_l = line.split(' ')
		for word in line_l:
			trans_word = strip_and_lower(word)
			if bool(trans_word):
				ret_list.append(trans_word)
	return ret_list

def markov_dict(l, pref_length):
	ret_d = dict()
	for x in range(len(l) - pref_length):
		prefix = ""
		for y in range(x, x + pref_length):
			prefix += " " + l[y]
		ret_d.setdefault(prefix, []).append(l[x + pref_length])
	return ret_d

def prefix_to_suffix(start, d):
	suffix = random.choice(d[start])
	pre_list = start.split()
	pre_list.append(suffix)
	pre_list = pre_list[1:]
	ret_string = ""
	for x in pre_list:
		ret_string += " " + x
	return ret_string

def markov_print(starting_prefix, n, in_dict):
	x = 0
	print(starting_prefix)
	while x < n:
		starting_prefix = prefix_to_suffix(starting_prefix, in_dict)
		print(starting_prefix.split()[-1])
		x += 1
if __name__ == '__main__':
	emma_words_list = words_list('emma.txt')
	emma_mark = markov_dict(emma_words_list, 2)
	starting_prefix = random.choice(list(emma_mark.keys()))
	markov_print(starting_prefix, 1000, emma_mark)




