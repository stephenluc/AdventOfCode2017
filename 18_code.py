def duet(instructions):
	last_sound = None
	registers = {}
	i = 0
	while i < len(instructions):
		step = instructions[i].split()
		if step[1] not in registers:
			registers[step[1]] = 0
		if len(step) == 3:
			try:
				step[2] = int(step[2])
			except:
				if step[2] not in registers:
					registers[step[2]] = 0
		if step[0] == 'snd':
			last_sound = registers[step[1]]
		elif step[0] == 'set':
			registers[step[1]] = step[2] if isinstance(step[2], int) else registers[step[2]]
		elif step[0] == 'add':
			registers[step[1]] += step[2] if isinstance(step[2], int) else registers[step[2]]
		elif step[0] == 'mul':
			registers[step[1]] *= step[2] if isinstance(step[2], int) else registers[step[2]]
		elif step[0] == 'mod':
			registers[step[1]] %= step[2] if isinstance(step[2], int) else registers[step[2]]
		elif step[0] == 'jgz':
			if registers[step[1]] > 0:
				i += step[2] if isinstance(step[2], int) else registers[step[2]]
				continue
		elif step[0] == 'rcv':
			if registers[step[1]] != 0:
				break
		i += 1
	print 'Part 1: ', last_sound

def part_2(instructions):
	total_sent = 0
	send = 0
	registers = {}
	i = 0
	while i < len(instructions) and i >= 0:
		step = instructions[i].split()
		try:
			step[1] = int(step[1])
		except:
			if step[1] not in registers:
				registers[step[1]] = 0
		if len(step) == 3:
			try:
				step[2] = int(step[2])
			except:
				if step[2] not in registers:
					registers[step[2]] = 0
		if step[0] == 'snd':
			send += 1
			total_sent += 1
		elif step[0] == 'set':
			registers[step[1]] = step[2] if isinstance(step[2], int) else registers[step[2]]
		elif step[0] == 'add':
			registers[step[1]] += step[2] if isinstance(step[2], int) else registers[step[2]]
		elif step[0] == 'mul':
			registers[step[1]] *= step[2] if isinstance(step[2], int) else registers[step[2]]
		elif step[0] == 'mod':
			registers[step[1]] %= step[2] if isinstance(step[2], int) else registers[step[2]]
		elif step[0] == 'jgz':
			if (isinstance(step[1], int) and step[1] > 0) or (registers[step[1]] > 0):
				i += step[2] if isinstance(step[2], int) else registers[step[2]]
				continue
		elif step[0] == 'rcv':
			if send > 0:
				send += -1
			else:
				break
		i += 1
	print 'Part 2: ', total_sent

from collections import deque

registers_0={"p":0,"counter":0}
registers_1={"p":1,"counter":0}
queue_for_0=deque()
queue_for_1=deque()

# runs until termination or wait state. Returns False on termination
def part_2(registers,queue_in,queue_out, instructions):

    def value(r):
        if r.isalpha():
            return registers.get(r,0)
        else:
            return int(r)

    #first_rcv_done=False
    while (registers["counter"]>=0) and (registers["counter"]<len(instructions)):
        parsed=instructions[registers["counter"]].strip().split()
        if parsed[0]=="rcv":
            if len(queue_in)==0:
                return True
            registers[parsed[1]]=queue_in.popleft()
        if parsed[0]=="jgz":
            if value(parsed[1])>0:
                registers["counter"]+=value(parsed[2])
                continue
        if parsed[0]=="snd":
            queue_out.append(value(parsed[1]))
            registers["sent"]=value("sent")+1
        if parsed[0]=="set":
            registers[parsed[1]]=value(parsed[2])
        if parsed[0]=="add":
            registers[parsed[1]]=value(parsed[1])+value(parsed[2])
        if parsed[0]=="mul":
            registers[parsed[1]]=value(parsed[1])*value(parsed[2])
        if parsed[0]=="mod":
            registers[parsed[1]]=value(parsed[1])%value(parsed[2])
        registers["counter"]+=1
    return False

f = open('18_input.txt', 'r')
instructions = f.readlines()

# Part 1
duet(instructions)

# Part 2

while True:
    if not part_2(registers_0,queue_for_0,queue_for_1, instructions): break
    if not part_2(registers_1,queue_for_1,queue_for_0, instructions): break
    if len(queue_for_0)==0 and len(queue_for_1)==0: break

print 'part 2: ', registers_1['sent']