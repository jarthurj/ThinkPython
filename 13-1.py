import string as str


def punctuation_mapping():
	punc = str.punctuation
	punc_dict = {}
	for x in punc:
		punc_dict[ord(x)] = None
	return punc_dict

def strip_and_lower(word):
	word.strip()
	trans_word = word.translate(table)
	trans_word.strip()
	trans_word.lower()
	return trans_word

if __name__ == '__main__':
	table = punctuation_mapping()
	words_dict = {}
	fin = open('Pride_and_Prejudice.txt', encoding='utf-8')
	for line in fin:
		line_l = line.split(' ')
		for word in line_l:
			print(strip_and_lower(word))