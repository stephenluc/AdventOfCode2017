def corruption_checksum(spreadsheet):
    sum = 0
    for row in spreadsheet:
        sum += max(row) - min(row)
    print sum

def part_2(spreadsheet):
    sum = 0
    for row in spreadsheet:
        for number in row:
            if [x % number for x in row].count(0) > 1:
                row.remove(number)
                sum += [x / number for x in row if x % number == 0][0]
                break
    print sum

f = open('02_input.txt', 'r')
spreadsheet = []
for line in f.readlines():
    spreadsheet.append(map(int, line.strip().split('\t')))

# Part 1
# corruption_checksum(spreadsheet)

# Part 2
# part_2(spreadsheet)
