def word_to_pro():
	wordpro = dict() # dictionary with word as key and pronunications as a list 
	proword = dict() #pronunciations as string with no spaces as keys the words as the values 
	wordlist = list()
	fin = open('cmudict.txt')

	for line in fin:
		line_list = line.strip().split(' ')
		word_pro_string = ["".join(line_list[1:]), line_list[0]] #lists to create the dictionaries
		if len(line_list[0]) == 5 or len(line_list[0]) == 4:
			wordpro[line_list[0]] = line_list[2:]
			proword[word_pro_string[0]] = word_pro_string[1]
			wordlist.append(line_list[0].strip())
	return wordpro, proword, wordlist



if __name__ == '__main__':
	wordpro, proword, wordlist = word_to_pro()

	for word in wordlist:
		no_first = word[1:].strip()
		no_second = (word[0] + word[2:]).strip()
		#print(word, no_first, no_second)
		if word in wordpro and no_first in wordpro and no_second in wordpro:

			if (wordpro[no_first] == wordpro[no_second] and
				wordpro[word] == wordpro[no_second] and 
				wordpro[word] == wordpro[no_first]):
				print(word, no_first, no_second, wordpro[word], wordpro[no_first], wordpro[no_second])