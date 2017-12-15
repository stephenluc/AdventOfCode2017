def dueling_generators(generators):
	factor_a = 16807
	factor_b = 48271
	denominator = 2147483647
	matches = 0
	a = generators['A']
	b = generators['B']
	for i in range(40000000):
		a = a * factor_a % denominator
		b = b * factor_b % denominator

		if bin(a)[-16:] == bin(b)[-16:]:
			matches += 1
	print matches

def part_2(generators):
	factor_a = 16807
	factor_b = 48271
	denominator = 2147483647
	matches = 0
	a = generators['A']
	b = generators['B']
	for i in range(5000000):
		while True:
			a = a * factor_a % denominator
			if a % 4 == 0: break

		while True:
			b = b * factor_b % denominator
			if b % 8 == 0: break

		if bin(a)[-16:] == bin(b)[-16:]:
			matches += 1
	print matches

f = open('15_input.txt', 'r')
lines = f.readlines()
generators = { 'A': 65 , 'B': 8921}
generators = { 'A': int(lines[0][-4:]) , 'B': int(lines[1][-3:])}

# dueling_generators(generators)

part_2(generators)