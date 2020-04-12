def twentyormore(word):
	if len(word) >= 20:
		print(word)

if __name__ == '__main__':
	fin = open('words.txt')
	for line in fin:
		twentyormore(line.strip())
