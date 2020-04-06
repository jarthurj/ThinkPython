import string

def find(word, letter):
	index = 0
	while index < len(word):
		if word[index] == letter:
			return index
		index += 1
	return -1

def find_wstart(word, letter, start):
	index = start
	while index < len(word):
		if word[index] == letter:
			return index
		index += 1
	return -1	

if __name__ == '__main__':
	print(find(string.ascii_lowercase, 'z'))
	print(find_wstart(string.ascii_lowercase, 'z', 6))