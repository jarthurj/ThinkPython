import string as str

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
	trans_word.strip()
	trans_word.lower()
	trans_word = trans_word.translate(table)
	return trans_word

if __name__ == '__main__':
	emma_dict = dict()
	words_set = set()
	fin = open('emma.txt', encoding='utf-8')
	for line in fin:
		line_l = line.split(' ')
		for word in line_l:
			trans_word = strip_and_lower(word)
			trans_word.strip().lower()

	fin = open('words.txt')
	for line in fin:
		words_set.add(line.strip().lower())
	print(len(emma_set))
	print(len(words_set))
	diff = emma_set - words_set
	print(len(diff))
	print(diff)

#