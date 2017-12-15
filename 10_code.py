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

def knot_hash(lengths):
    n = 256
    #n = 5
    #lengths = [3, 4, 1, 5]
    circular_list = range(n)
    
    curr = 0
    skip = 0
    for sub_length in lengths:
        circular_list = reverse_circular_sublist(circular_list, curr, curr + sub_length - 1)
        curr = (curr + sub_length + skip) % n
        skip += 1

    print circular_list[0] * circular_list[1]

def part_2(lengths):
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

    print ''.join(dense_hash)



f = open('10_input.txt', 'r')
lengths = map(int, f.readline().strip().split(','))
f.close()

# Part 1
knot_hash(lengths)

ascii_lengths = [ord(x) for x in open('10_input.txt','r').read().rstrip()]
ascii_lengths.extend([17,31,73,47,23])

# Part 2
part_2(ascii_lengths)
