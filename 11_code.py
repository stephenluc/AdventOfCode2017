def hex_ed(directions):
	x = 0
	y = 0
	z = 0

	max_steps = 0

	for d in directions:
		if d == 'n':
			y += 1
			z += -1
		elif d == 'nw':
			y += 1
			x += -1
		elif d == 'ne':
			x += 1
			z += -1
		elif d == 's':
			z += 1
			y += -1
		elif d == 'sw':
			z += 1
			x += -1
		elif d == 'se':
			x += 1
			y += -1

		max_steps = max(max_steps, (abs(x) + abs(y) + abs(z)) / 2)

	# Part 1 answer
	print 'Fewest steps to find child:', (abs(x) + abs(y) + abs(z)) / 2
	# Part 2 answer
	print 'Max steps achieved: ', max_steps

f = open('11_input.txt', 'r')
directions = f.readline().split(',')

# Part 1 and Part 2
hex_ed(directions)