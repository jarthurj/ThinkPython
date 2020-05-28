class Point(object):
	x = 0
	y = 0

	def distance(p1, p2):
		x_part = (p1.x - p2.x) ** 2
		y_part = (p1.y - p2.y) ** 2

		distance = (x_part + y_part) ** (1 / 2)

		return distance
	def print_point(self):
		print("(" + str(self.x) + "," + str(self.y) + ")")
if __name__ == '__main__':
	tp00 = Point()
	tp00.x = 0
	tp00.y = 0

	tp34 = Point()
	tp34.x = 3
	tp34.y = 4 
	print("0,0 to 0,0: " + str(Point.distance(tp00, tp00)))

	print("0,0 to 3,4 :" + str(Point.distance(tp00, tp34)))
