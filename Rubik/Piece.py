class Piece(object):
	def __init__(self, color_and_vectors=([None,0],[None,0],[None,0])):
		self.vectors = color_and_vectors

	def __str__(self):
		return str(self.vectors)

	def coord_to_vector(coord):
		coords = {
					(1,1,1):([None,-1],[None,-1],[None,-1]),
					(1,1,2):([None,-1],[None,-1],[None,0]),
					(1,2,1):([None,-1],[None,0],[None,-1]),
					(1,2,1):([None,-1],[None,0],[None,-1]),
					(2,1,1):([None,0],[None,-1],[None,-1]),
					(1,1,3):([None,-1],[None,-1],[None,1]),
					(1,2,2):([None,-1],[None,0],[None,0]),
					(1,3,1):([None,-1],[None,1],[None,-1]),
					(2,1,2):([None,0],[None,-1],[None,0]),
					(2,2,1):([None,0],[None,0],[None,-1]),
					(3,1,1):([None,1],[None,-1],[None,-1]),
					(1,2,3):([None,-1],[None,0],[None,1]),
					(1,3,2):([None,-1],[None,1],[None,0]),
					(2,1,3):([None,0],[None,-1],[None,1]),
					(2,3,1):([None,0],[None,1],[None,-1]),
					(3,1,2):([None,1],[None,-1],[None,0]),
					(3,2,1):([None,1],[None,0],[None,-1]),
					(1,3,3):([None,-1],[None,1],[None,1]),
					(2,2,3):([None,0],[None,0],[None,1]),
					(2,3,2):([None,0],[None,1],[None,0]),
					(3,1,3):([None,1],[None,-1],[None,1]),
					(3,2,2):([None,1],[None,0],[None,0]),
					(3,3,1):([None,1],[None,1],[None,-1]),
					(2,3,3):([None,0],[None,1],[None,1]),
					(3,2,3):([None,1],[None,0],[None,1]),
					(3,3,2):([None,1],[None,1],[None,0]),
					(3,3,3):([None,1],[None,1],[None,1])}

		return coords[coord]

	def type(self):
		num_vectors = 0
		for x in self.vectors:
			if x[1] != 0:
				num_vectors += 1
		if num_vectors == 1:
			return "center"
		elif num_vectors == 2:
			return "edge"
		elif num_vectors == 3:
			return "corner"

if __name__ == '__main__':
	print("pieces")