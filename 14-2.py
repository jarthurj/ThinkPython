import random

def sed(pattern, replace, doc1, doc2):
	pattern_list = pattern.split()
	doc1_word_list = doc_lister(doc1)
	


def doc_lister(doc1):
	fin = open(doc1)
	doc_list = list()
	for line in fin:
		line_list = line.split()
		for word in line_list:
			doc_list.append(word)
	return doc_list

def words_to_list():
	fin = open('words.txt')
	words_list = list()	
	for line in fin:
		words_list.append(line.strip())	
	return words_list


def random_doc():
	file_name = 'randomtext.txt'
	words_list = words_to_list()
	new_doc = open(file_name, 'w')
	num_lines = random.randint(0, 100)
	for x in range(num_lines):
		words_per_line = random.randint(0, 10)
		for y in range(words_per_line):
			r_word = random.choice(words_list)
			new_doc.write(r_word + " ")
		new_doc.write('\n')
	return file_name



if __name__ == '__main__':
	x = random_doc()