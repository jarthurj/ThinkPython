
coord_d = dict()
for x in range(1,4):
	for y in range(1,4):
		for z in range(1,4):
			coord_d[(x,y,z)] = None
del coord_d[(2,2,2)]

l = list()
for x in coord_d:
	tot = 0
	for y in x:
		tot += y
	l.append((tot, x))
l.sort()
for x in l:
	print(x)