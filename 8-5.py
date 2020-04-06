def count(word, letter):
	count = 0
	for char in word:
		if char == letter:
			count += 1
	return count


if __name__ == '__main__':
	print(count("butts","t"))