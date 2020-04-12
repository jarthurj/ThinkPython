import string
import numpy as np 
from itertools import permutations

def avoids(word, letters):
	for char in letters:
		if char in word:
			return False
	return True
 
def permute_alphabet():
	alphabet_list = list(string.ascii_lowercase)
	perm = permutations(alphabet_list, 5)
	permset = set()
	a = np.array("abcde")
	for i in perm:
		z = "".join(sorted(i))
		permset.add(z)
	for x in permset:
		b = np.array(x)
		a = np.array
	return tuple(permset)

def permalphadict():
	permlist = permute_alphabet()
	empdict = {}
	for x in permlist:
		empdict.update({x:0})
	return empdict

if __name__ == '__main__':
	permlist = permute_alphabet()
	permdict = permalphadict()
	fin = open('words.txt')
	linenumber = 1
	for line in fin:
		print(linenumber)
		for x in permlist:
			if avoids(line, x):
				permdict[x] += 1
		linenumber += 1
	final_list = [(k,v) for v,k in permdict.items()]
	final_list.sort()
	print(final_list)
