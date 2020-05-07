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

	words_dict = {}
	words_histogram_list = []
	fin = open('Pride_and_Prejudice.txt', encoding='utf-8')
	for line in fin:
		line_l = line.split(' ')
		for word in line_l:
			trans_word = strip_and_lower(word)
			words_dict[trans_word.strip().lower()] = words_dict.get(trans_word.strip().lower(), 0) + 1
	
	total = 0
	for x in words_dict:
		total += words_dict[x]
		words_histogram_list.append((words_dict[x], x))
	words_histogram_list.sort(reverse=True)
	for y in range(0, 20):
		print(words_histogram_list[y])
	print(total)