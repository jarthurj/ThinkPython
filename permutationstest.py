import string 
from itertools import permutations

alphabet_list = list(string.ascii_lowercase)
perm = permutations(alphabet_list, 5)
permset = set()
for i in perm:
	z = tuple(sorted(i))
	permset.add(z)
print(len(permset))