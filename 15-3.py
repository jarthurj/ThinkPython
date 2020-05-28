from Rectangle import Rectangle
if __name__ == "__main__":
	box = Rectangle()
	box.corner.x = 0
	box.corner.y = 0
	box.width = 5
	box.height = 5

	box2 = box.move_and_copy_rectangle(5, 5)

	box2.print_rect()
	box.print_rect()
	# print(box is box2)
	# print(box.corner is box2.corner)