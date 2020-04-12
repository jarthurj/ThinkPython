def triple_double(word):
	for x in range(0, len(word) - 5):
		test_word = word[x: x + 6]
		if test_word[0] == test_word[1] and test_word[2] == test_word[3] and test_word[4] == test_word[5]:
			print(word)
if __name__ == '__main__':
	fin = open('words.txt')
	for line in fin:
		if triple_double(line.strip()):
			print(line.strip())