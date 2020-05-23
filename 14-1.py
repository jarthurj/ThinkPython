import os

dir_to_walk = 'C:\\Users\\Johnny\\Desktop\\PythonLearning'

walker = os.walk(dir_to_walk)

for x, y, z in walker:
	print(x, y, z)
	
	




		