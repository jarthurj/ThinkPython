import time

def dict_words():
	fin = open('words.txt')
	d_words = {}
	for line in fin:
		d_words[line.strip()] = 0
	return d_words

def words_list():
	fin = open('words.txt')
	out_list = list()
	for line in fin:
		out_list.append(line.strip())
	return out_list	

def bisect(in_list, search_word):
	middle_index = len(in_list) //  2
	if in_list[middle_index] == search_word:
		return True
	if in_list[middle_index] > search_word:		
		return bisect(in_list[:middle_index], search_word)
	if in_list[middle_index] < search_word:
		return bisect(in_list[middle_index:], search_word)
	return False
if __name__ == '__main__':
	dwords = dict_words()
	lwords = words_list()

	start_time = time.time()
	print('butt' in lwords)
	time1 = time.time() - start_time

	start_time = time.time()
	print(bisect(lwords, 'butt'))
	time2 = time.time() - start_time

	start_time = time.time()
	print('butt' in dwords)
	time3 = time.time() - start_time

	print(time1)
	print(time2)
	print(time3)