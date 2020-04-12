def uses_all(word, letters):
	truth_count = 0
	sing_word = singleton_word(word)
	for char_x in letters:
		for char_y in sing_word:
			if char_x == char_y:
				truth_count += 1
	#print(truth_count, len(word))
	if truth_count == len(letters):
		return True 
	else:
		return False

def singleton_word(word):
	singleton_word = ""
	for x in word:
		singleton_word += x
		count = 0
		for y in singleton_word:
			if x == y:
				count += 1
		if count > 1:
			singleton_word = singleton_word[:-1]
	return singleton_word

def uses_all2(word, letters):
	for char_x in letters:
		if char_x not in word:
			return False
	return True

if __name__ == '__main__':
	fin = open('words.txt')
	count = 0
	chars = "aeiou"
	for line in fin:
		if uses_all2(line.strip(), chars):
			count += 1
			print(line, count)
