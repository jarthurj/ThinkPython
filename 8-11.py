def rotate_word(word, rotator):
	rotated_word = ""
	for char in word:
		if ord(char) > ord('z') - rotator:
			new_ord = ord(char) + rotator - ord('z') + ord('a') - 1
		else:
			new_ord = ord(char) + rotator
		rotated_word += chr(new_ord)
	return rotated_word


if __name__ == '__main__':
	print(rotate_word("q", 13))