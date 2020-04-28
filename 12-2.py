import random

def sort_by_length(words):
	t = []
	y = []
	for word in words:
		t.append((len(word),random.random(),word))
	t.sort()
	for x in t:
		y.append((x[0], x[2]))
	return y

	return res
if __name__ == '__main__':
	fin = open('words.txt')
	words_list = []
	for line in fin:0
		words_list.append(line.strip())

	print(sort_by_length(words_list))
