# testing a way of choosing random words 
#The words will be chosen from a dictionary with words as the key
# and the frequincies as the value. The total will kept separate
import random

d = {"butt": 10000, "easy":5000, "and":10000, "key":25000}
total = 50000
l = []
for x in d:
	l.extend([x] * d[x])
dd = dict()
ld = dict()
for x in range(1000000):
	choice = False
	while not choice:
		rand_key = random.choice(list(d.keys()))
		second_choice = random.randint(1,50000)
		if second_choice <= d[rand_key]:
			choice = True
			dd[rand_key] = dd.get(rand_key, 0) + 1
			#print(dd)

for x in range(1000000):
	rand_word = random.choice(l)
	ld[rand_word] = ld.get(rand_word, 0) + 1

print("Dict Double Choice")
print(dd)
print("List Random Choice")
print(ld)