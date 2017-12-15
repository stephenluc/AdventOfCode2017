def packet_scanners(firewall):
	scanner = 0
	severity = 0
	for index, wall in enumerate(firewall):
		location = (2 * (wall - 1))
		if not location < 0:
			if scanner % (2 * (wall - 1)) == 0:
				severity += wall * index
		scanner += 1
	print severity

def part_2(firewall):
	wait_time = 2
	while True:
		get_caught = False
		scanner = wait_time
		for index, wall in enumerate(firewall):
			location = (2 * (wall - 1))
			if not location < 0:
				if scanner % (2 * (wall - 1)) == 0:
					get_caught = True
					break
			scanner += 1

		if get_caught:
			wait_time += 2
		else:
			break
	print wait_time

f = open('13_input.txt', 'r')
lines = [x.split(': ') for x in f.readlines()]
firewall = [0] * (int(lines[-1][0]) + 1)

for layer in lines:
	firewall[int(layer[0])] = int(layer[1])

# Part 1
packet_scanners(firewall)

# Part 2
part_2(firewall)