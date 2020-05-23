import random

def sed(replace, doc1, doc2):
	doc1_word_list, replacer = doc_lister(doc1)



def doc_lister(doc1):
	fin = open(doc1)
	doc_list = list()
	line_d = dict()
	count = 0

	for line in fin:
		line_list = line_d[count] = line.split()
		count += 1
		for word in line_list:
			doc_list.append(word)
	random_line = line_d[random.choice(list(line_d.keys()))]

	return doc_list, random_line

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
	new_file = random_doc()
	sed("fuck fuck fuck", new_file, "processed_file.txt")