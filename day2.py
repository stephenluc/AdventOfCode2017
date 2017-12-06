def corruption_checksum(spreadsheet):
    sum = 0
    for row in spreadsheet:
        sum += max(row) - min(row)
    print sum

f = open('02_input.txt', 'r')
spreadsheet = []
for line in f.readlines():
    spreadsheet.append(map(int, line.strip().split('\t')))

corruption_checksum(spreadsheet)
