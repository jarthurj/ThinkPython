def find_wstart(word, letter, start):
	index = start
	while index < len(word):
		if word[index] == letter:
			return index
		index += 1
	return -1	

def count(word, letter):
	count = 0
	index = 0
	while index != -1:
		index = find_wstart(word, letter, index + 1)
		if index != -1: count += 1
	return count


if __name__ == '__main__':
	print(count("buts","t"))