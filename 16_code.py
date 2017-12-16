import string

def permutation_promenade(reps, dance):
	programs = list(string.ascii_lowercase)[:16]
	seen_dance = []
	for i in range(reps):
		if ''.join(programs) in seen_dance:
			print seen_dance[reps % i]
			return
		seen_dance.append(''.join(programs))
		for step in dance:
			if step[0] == 's':
				spin = int(''.join(step[1:]))
				programs = programs[-spin:] + programs[:-spin]
			elif step[0] == 'x':
				a,b = step[1:].split('/')
				index_a = int(a)
				index_b = int(b)
				programs[index_a], programs[index_b] = programs[index_b], programs[index_a]
			elif step[0] == 'p':
				a,b = step[1:].split('/')
				index_a = programs.index(a)
				index_b = programs.index(b)
				programs[index_a], programs[index_b] = programs[index_b], programs[index_a]

	print ''.join(programs)


f = open('16_input.txt', 'r')
dance = f.readline().split(',')

# Part 1
permutation_promenade(1, dance)

# Part 2
permutation_promenade(1000000000, dance)