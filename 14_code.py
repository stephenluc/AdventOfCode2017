def reverse_circular_sublist(circ_list, start, end):
    sublist = []
    for i in range(start,end+1):
        sublist.append(circ_list[i % len(circ_list)])
    reverse = list(reversed(sublist))
    j=0
    for i in range(start,end+1):
        circ_list[i % len(circ_list)] = reverse[j]
        j+=1
    return circ_list

def get_groups(disk):
	n = len(disk)
	m = len(disk[0])
	discoveredX = [[False for i in range(n)] for j in range(m)] 
	totalX = 0
    
	for x in range(n):
		for y in range(m):
			if (disk[x][y] == '1' and not discoveredX[x][y]):
				totalX += 1
				checkSurrondings(disk, discoveredX, x, y)
	return totalX

def checkSurrondings(matrix, discoveredX, x, y):
	if not(x < 0 or y < 0) and x < len(matrix[0]) and y < len(matrix):
		if matrix[x][y] == '1' and not discoveredX[x][y]:
			discoveredX[x][y] = True
			checkSurrondings(matrix, discoveredX, x+1, y)
			checkSurrondings(matrix, discoveredX, x-1, y)
			checkSurrondings(matrix, discoveredX, x, y+1)
			checkSurrondings(matrix, discoveredX, x, y-1)

def disk_defragmentation(ascii):
	used_space = 0
	disk =[]
	for i in range(128):
		if i < 10:
			lengths = ascii + [ord('-'), ord('{}'.format(i)), 17,31,73,47,23]
		elif i < 100:
			i = str(i)
			lengths = ascii + [ord('-'), ord(i[0]), ord(i[1]),17,31,73,47,23]
		else:
			i = str(i)
			lengths = ascii + [ord('-'), ord(i[0]), ord(i[1]), ord(i[2]),17,31,73,47,23]
		curr = 0
		skip = 0
		n = 256
		circular_list = range(n)
		for run in range(64):        
			for sub_length in lengths:
				circular_list = reverse_circular_sublist(circular_list, curr, curr + sub_length - 1)
				curr = (curr + sub_length + skip) % n
				skip += 1

		dense_hash = []
		for reduce_set in range(16):
			subset = circular_list[16 * reduce_set: 16 * (reduce_set + 1)]
			dense_hash.append('%02x'%reduce((lambda x,y: x ^ y),subset))

		binary = list(bin(int(''.join(dense_hash), 16))[2:])
		binary = ['0'] * (128 - len(binary)) + binary if len(binary) < 128 else binary
		disk.append(binary)
		used_space += sum([int(x) for x in binary])
	print 'Part 1: ', used_space
	print 'Part 2: ', get_groups(disk)

ascii_lengths = [ord(x) for x in open('14_input.txt','r').read().rstrip()]

disk_defragmentation(ascii_lengths)