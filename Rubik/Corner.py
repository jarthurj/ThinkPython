class Corner(object):
	def __init__(self, color_and_vectors=([None,0],[None,0],[None,0])):
		self.color_and_vectors = color_and_vectors

	def __str__(self):
		return str(self.color_and_vectors)

	def coord_to_vector(coord):

		vector = ([None, 0], [None, 0], [None, 0])
		for x in range(len(coord)):
			if coord[x] == 1:
				vector[x][1] = -1
			elif coord[x] == 3:
				vector[x][1] = 1
		return vector
				
