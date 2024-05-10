import turtle

running = True

while running: 
	print("Enter the following below: triangle, square, pentagon, hexagon, pentagram, or exit: ")
	entered = input()

#triangle
	if entered == 'triangle':
		for i in range(3):
			turtle.forward(100)
			turtle.right(120)

#square
	elif entered == 'square':
		for i in range(4):
			turtle.forward(100)
			turtle.right(90)

#pentagon
	elif entered == 'pentagon':
		for i in range(5):
			turtle.forward(100)
			turtle.right(72)

#hexagon
	elif entered == 'hexagon':
		for i in range(6):
			turtle.forward(100)
			turtle.right(60)

# #pentagram 
# 	elif entered == 'pentagram':
# 		for i in range(5):
# 			turtle.forward(100)
# 			turtle.right(36)
# 			turtle.forward(100)

	elif entered == 'exit':
		running = False
		print('exiting ...')

	else:
		print('not a command')

