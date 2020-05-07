import string as str

def punctuation_mapping():
	punc = str.punctuation + '”' + '“' + '—'+ '—'+ '‘' + '’' + '”'
	punc_dict = {}
	for x in punc:
		punc_dict[ord(x)] = None
	return punc_dict

def words_dict():
	fin = open('words.txt')
	ret = dict()
	for line in fin:
		ret[line.strip()] = None
	return ret

def strip_and_lower(word):
	table = punctuation_mapping()
	word.strip()
	trans_word = word.translate(table)
	trans_word.strip()
	trans_word.lower()
	trans_word = trans_word.translate(table)
	return trans_word

if __name__ == '__main__':
	words_dict = {}
	words_histogram_list = []
	words_dot_text = words_dict()
	fin = open('Pride_and_Prejudice.txt', encoding='utf-8')
	for line in fin:
		line_l = line.split(' ')
		for word in line_l:
			trans_word = strip_and_lower(word)
			words_dict[trans_word.strip().lower()] = words_dict.get(trans_word.strip().lower(), 0) + 1
	del words_dict['']
	# total = 0
	# for x in words_dict:
	# 	total += words_dict[x]
	for x in words_dict:
		if x not in


	print(total)