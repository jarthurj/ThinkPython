class Center(object):
	def __init__(self, color_and_vectors=([None,0],[None,0],[None,0])):
		self.color_and_vectors = color_and_vectors

	def __str__(self):
		return str(self.color_and_vectors)

	def coord_to_vector(coord):
		y = 0 
		vector = ([None, 0], [None, 0], [None, 0])
		for x in coord:
			y += x

		if y == 5:
			for x in coord:
				if x == 2:
					vector[coord.index(x)][1] = 0
				else:
					vector[coord.index(x)][1] = -1
						
		elif y == 7:
			for x in coord:
				if x == 3:
					vector[coord.index(x)][1] = 1
				else:
					vector[coord.index(x)][1] = 0

		return vector

