def has_no_e(word):
	if 'e' not in word:
		print(word)


if __name__== '__main__':
	fin = open('words.txt')
	for line in fin:
		has_no_e(line)