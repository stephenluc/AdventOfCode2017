def spinlock(steps):
	circular_buffer = [0]
	position = 0
	for i in range(1, 2017 + 1):
		position = (position + 1 + steps) % i
		circular_buffer.insert(position + 1, i)

	print 'Part 1: ', circular_buffer[position + 2]

def part_2(steps):
	position = 0
	for i in range(1, 50000000 + 1):
		position = 1+ (position + steps) % i
		if position == 1:
			vale_after_0 = i

	print 'Part 2: ', vale_after_0


f = open('17_input.txt', 'r')
steps = int(f.readline())
# Part 1
spinlock(steps)

# Part 2
part_2(steps)