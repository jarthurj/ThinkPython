from itertools import permutations
# from Edge import Edge
# from Center import Center
# from Corner import Corner
from Piece import Piece
class Rubik(object):
	def __init__(self):
		self.cube = Rubik.color_cube()

	def __str__(self):
		return str(self.cube)
	def make_coords():
		coord_d = dict()
		for x in range(1,4):
			for y in range(1,4):
				for z in range(1,4):
					coord_d[(x,y,z)] = None
		del coord_d[(2,2,2)]
		return coord_d

	# def make_corners():
	# 	per_list = list(permutations([1,1,3])) + list(permutations([3,3,1])) + [(3,3,3),(1,1,1)]
	# 	corn_set = set()
	# 	for x in per_list:
	# 		corn_set.add(x)
	# 	corn_d = dict()
	# 	for x in corn_set:
	# 		vector = Corner.coord_to_vector(x)
	# 		corn_d[x] = Corner(vector)
	# 	return corn_d

	# # def make_centers():
	# # 	cent_list = list(permutations([2,2,3])) + list(permutations([2,2,1]))
	# # 	cent_set = set()
	# # 	for x in cent_list:
	# # 		cent_set.add(x)
	# # 	cent_d = dict()
	# # 	for x in cent_set:
	# # 		vector = Center.coord_to_vector(x)
	# # 		cent_d[x] = Center(vector)
	# # 	return cent_d

	# # def make_edges():
	# # 	edge_list = list(permutations([1,2,3])) + list(permutations([2,1,1])) + list(permutations([2,3,3]))
	# # 	edge_set = set()
	# # 	for x in edge_list:
	# # 		edge_set.add(x)
	# # 	edge_d = dict()
	# # 	for x in edge_set:
	# # 		vector = Edge.coord_to_vector(x)
	# # 		edge_d[x] = Edge(vector)
	# # 	return edge_d

	# def make_cube():
	# 	cube = Rubik.make_corners()
	# 	cube.update(Rubik.make_centers())
	# 	cube.update(Rubik.make_edges())
	# 	return cube

	def make_cube2():
		coords_list = Rubik.make_coords()
		cube = dict()
		for x in coords_list:
			vector = Piece.coord_to_vector(x)
			cube[x] = Piece(vector)
		# cents = 0
		# corns = 0
		# edges = 0
		# temp_list = []
		# for y in cube:
		# 	temp_list.append((sum(list(y)), y, str(cube[y]), Piece.type(cube[y])))
		# 	if Piece.type(cube[y]) == 'center':
		# 		cents += 1
		# 	if Piece.type(cube[y]) == 'edge':
		# 		edges += 1
		# 	if Piece.type(cube[y]) == 'corner':
		# 		corns += 1
		# temp_list.sort()
		# for x in temp_list:
		# 	print(x)
		# print("Centers:" + str(cents) + " Edges:" + str(edges) + " Corners:" + str(corns))

		return cube

	def color_cube():
		cube = Rubik.make_cube2()
		for x in cube:
			if x[1] == 1 and cube[x].vectors[1][1] == -1:
				cube[x].vectors[1][0] = 'Red'
			if x[1] == 3 and cube[x].vectors[1][1] == 1:
				cube[x].vectors[1][0] = 'Orange'
			if x[0] == 1 and cube[x].vectors[0][1] == -1:
				cube[x].vectors[0][0] = 'Green'
			if x[0] == 3 and cube[x].vectors[0][1] == 1:
				cube[x].vectors[0][0] = 'Blue'
			if x[2] == 3 and cube[x].vectors[2][1] == 1:
				cube[x].vectors[2][0] = 'White'
			if x[2] == 1 and cube[x].vectors[2][1] == -1:
				cube[x].vectors[2][0] = 'Yellow'
		cents = 0
		corns = 0
		edges = 0			
		for y in cube:
			
			print(y,cube[y], Piece.type(cube[y]))
			if Piece.type(cube[y]) == 'center':
				cents += 1
			if Piece.type(cube[y]) == 'edge':
				edges += 1
			if Piece.type(cube[y]) == 'corner':
				corns += 1
		print("Centers:" + str(cents) + "Edges:" + str(edges) + "Corners:" + str(corns))
		return cube
if __name__ == "__main__":
	x = Rubik()
	# for y in x.cube:
	# 	print(y, x.cube[y])

