import time

fin = open('words.txt')

out_list = list()
start_time = time.time()

for line in fin:
	print(line)
	#temp = [line]
	out_list.append(line)
elapsed_time = time.time() - start_time
print("append", elapsed_time)


