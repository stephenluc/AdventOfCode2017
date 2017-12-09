def stream_processing(stream):
    score = 0
    groups = 0
    in_garbage = False
    garbage_count = 0
    i = 0
    while i < len(stream):
        if stream[i] == '!':
            i += 2
            continue
        if in_garbage:
            if stream[i] == '>':
                in_garbage = False
            else:
                garbage_count += 1
        elif stream[i] == '<':
            in_garbage = True
        elif stream[i] == '{':
            groups += 1
        elif stream[i] == '}':
            score += groups
            groups += -1

        i += 1

    # Part 1 answer
    print 'Number of groups: ', score
    # Part 2 answer
    print 'Garbage removed: ', garbage_count

f = open('09_input.txt', 'r')
stream = f.readline()

# Part 1 and Part 2
stream_processing(stream)
