from Rectangle import Rectangle

if __name__ == "__main__":
	box = Rectangle()
	box.corner.x = 0
	box.corner.y = 0
	box.width = 5
	box.height = 5

	box.move_rectangle(5, 5)
	box.print_rect()