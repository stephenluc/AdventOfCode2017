import re
import operator

def heard_you_like_registers(instructions):
    registers = {}
    
    pattern = re.compile('([a-z]+) (inc|dec) (\-?\d+) if ([a-z]+) ([\!\<\>\=]=?) (-?\d+)')

    ops = {
        '!=': operator.ne,
        '<' : operator.lt,
        '<=': operator.le,
        '>' : operator.gt,
        '>=': operator.ge,
        '==': operator.eq,
    }
    maximum = 0
    for row in instructions:
        match = pattern.search(row)
        if match.group(1) not in registers:
            registers[match.group(1)] = 0
        if match.group(4) not in registers:
            registers[match.group(4)] = 0
        multiplier = 1 if match.group(2) == 'inc' else -1
        modify_by = int(match.group(3))
        condition = int(match.group(6))

        operate = match.group(5)

        registers[match.group(1)] += multiplier * modify_by if ops[operate](registers[match.group(4)], condition) else 0

        maximum = max(max([i for i in registers.values()]), maximum)
    
    # Part 1 answer
    print 'maximum value at end: ', max([i for i in registers.values()]) 
    # Part 2 answer 
    print 'maximum value ever recorded: ', maximum

f = open('08_input.txt', 'r')
instructions = f.readlines()

# Part 1 and 2
heard_you_like_registers(instructions)


