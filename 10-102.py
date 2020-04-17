import time

fin = open('words.txt')

out_list = list()
start_time = time.time()

for line in fin:
	print(line)
	out_list += [line]
elapsed_time = time.time() - start_time
print("+=:", elapsed_time)


