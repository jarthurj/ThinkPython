def is_abecedarian(word):
	for x in range(0, len(word) - 1):
		if word[x] > word[x + 1]:
			return False
	return True

def is_abecedarian2(word):
	if word == "".join(sorted(word)):
		return True
	return False

if __name__ == '__main__':
	fin = open('words.txt')

	for line in fin:
		if is_abecedarian2(line.strip()):
			print(line.strip())