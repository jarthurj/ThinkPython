def words_list():
	fin = open('words.txt')
	out_list = list()
	for line in fin:
		out_list.append(line.strip())
	return out_list	

def bisect(in_list, search_word):
	middle_index = len(in_list) //  2
	print(in_list[middle_index], middle_index)
	if in_list[middle_index] == search_word:
		return True
	elif in_list[middle_index] > search_word:		
		return bisect(in_list[:middle_index], search_word)
	elif in_list[middle_index] < search_word:
		return bisect(in_list[middle_index:], search_word)
	return False

def bisect_index(in_list, search_word):
	running_index = 1
	while True:
		middle_index = len(in_list) //  2
		if in_list[middle_index] == search_word:
			return running_index
		elif len(in_list) == 1 and in_list[0] != search_word:
			print('none return')
			return None
		elif in_list[middle_index] > search_word:		
			in_list = in_list[:middle_index]
		elif in_list[middle_index] < search_word:
			in_list = in_list[middle_index:]
			running_index += middle_index

if __name__ == '__main__':
	w_list = words_list()
	for word in w_list:
		if bisect(w_list, word[:-1]):
			print(word, word[:-1])