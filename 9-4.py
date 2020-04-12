def uses_only(word, letters):
	truth_count = 0
	for char_x in word:
		for char_y in letters:
			if char_x == char_y:
				truth_count += 1
	#print(truth_count, len(word))
	if truth_count == len(word):
		return True 
	else:
		return False


def uses_only2(word, letters):
	for char_x in word:
		if char_x not in letters:
			return False
	return True

if __name__ == '__main__':
	fin = open('words.txt')
	chars = "acefhlo"
	for line in fin:

		if uses_only2(line.strip(), chars):
			print(line)
