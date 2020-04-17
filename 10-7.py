def is_anagram(word1, word2):
	x1 = word1.split()
	x1.sort()
	x2 = word1.split()
	x2.sort()
	if x1 == x2:
		return True
	else:
		return False
if __name__ == '__main__':
	word1 = "abcde"
	word2 = "edcba"
	word3 = "fffff"
	#print(is_anagram(word1, word2))
	#print(is_anagram(word1, word3))