import time

def words_list():
	fin = open('words.txt')
	out_list = list()
	for line in fin:
		out_list.append(line.strip())
	return out_list	

def bisect(in_list, search_word):
	middle_index = len(in_list) //  2
	if len(in_list) == 0:
		return False 
	elif in_list[middle_index] == search_word:
		return True
	elif len(in_list) == 1 and in_list[0] != search_word:
		return False
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

# 
# 	for x in w_list:
# 		temp_word1 = ""
# 		temp_word2 = ""
# 		for y in range(0, len(x)):
# 			if y % 2 == 0:
# 				temp_word1 += x[y]
# 			else:
# 				temp_word2 += x[y]
# 		if bisect(w_list, temp_word1) and bisect(w_list, temp_word2):
# 			print(temp_word1, temp_word2)

	w_list = words_list()
	for x in w_list:
		temp_word1 = ""
		temp_word2 = ""
		temp_word3 = ""
		for y in range(0, len(x)):
			if y % 3 == 0:
				temp_word1 += x[y]
			elif y % 3 == 1:
				temp_word2 += x[y]
			elif y % 3 == 2:
				temp_word3 += x[y]
		if bisect(w_list, temp_word1) and bisect(w_list, temp_word2) and bisect(w_list, temp_word3):
			print(x, temp_word1, temp_word2, temp_word3)
