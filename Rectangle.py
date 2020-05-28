from Point import Point
import copy

class Rectangle(object):
	corner = Point()
	width = 0
	height = 0

	def move_rectangle(self, dx, dy):
		self.corner.x += dx
		self.corner.y += dy

	def print_rect(self):
		print("Corner:")
		self.corner.print_point()
		print("Width:")
		print(str(self.width))
		print("Height:")
		print(str(self.height))

	def move_and_copy_rectangle(rect, dx, dy):
		new_rect = copy.deepcopy(rect)
		new_rect.corner = copy.deepcopy(rect.corner)
		new_rect.corner.x += dx
		new_rect.corner.y += dy
		return new_rect
