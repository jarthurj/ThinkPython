from Point import Point
"""
If the __name__==__main__ is for test code then I just copied it from the class file
"""
if __name__ == '__main__':
	tp00 = Point()
	tp00.x = 0
	tp00.y = 0

	tp34 = Point()
	tp34.x = 3
	tp34.y = 4 
	print("0,0 to 0,0: " + str(Point.distance(tp00, tp00)))

	print("0,0 to 3,4 :" + str(Point.distance(tp00, tp34)))

