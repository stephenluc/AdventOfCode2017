import re

class Program:
    def __init__(self, name, weight):
        self.parent = None
        self.name = name
        self.weight = weight
        self.disc = []

    def add_to_disc(self, sub_tower):
        sub_tower.set_parent(self)
        self.disc.append(sub_tower)

    def set_parent(self, parent):
        self.parent = parent

    def get_weight(self):
        return self.weight

    def get_subtowers(self):
        return self.disc

    def childrens_weights(self):
        total_weights = 0
        for child in self.disc:
            total_weights += child.get_weight() + child.childrens_weights()
        return total_weights

    def __str__(self):
        return self.name

def get_root(child):
    if child.parent:
        return get_root(child.parent)
    return child

def recursive_circus(tower):
    programs = {}
    for program in tower:
        if not program['name'] in programs:
            programs[program['name']] = Program(program['name'], program['weight'])
    tower = [x for x in tower if x['children']]
    for program in tower:
        for children in program['children'].split(', '):
            programs[program['name']].add_to_disc(programs[children])

    return get_root(programs[tower[0]['name']])

def part_2(root):
    if not root.get_subtowers():
        return -1
    weights = []
    for children in root.get_subtowers():
        weights.append(children.get_weight() + children.childrens_weights())
    if not max(weights) == min(weights):
        if weights.count(min(weights)) > 1:
            if part_2(root.get_subtowers()[weights.index(max(weights))]) == -1:
                print root.get_subtowers()[weights.index(max(weights))].get_weight() - (max(weights) - min(weights))
        else:
            if part_2(root.get_subtowers()[weights.index(min(weights))]) == -1:
                print root.get_subtowers()[weights.index(min(weights))].get_weight() + (max(weights) - min(weights))
    else:
        return -1

f = open('07_input.txt', 'r')
tower = []
pattern = re.compile('([a-z]+) \((\d+)\)( \-\> (.+))?')

for line in f.readlines():
    found = pattern.search(line)
    tower.append({'name': found.group(1), 'weight': int(found.group(2)), 'children': found.group(4)})

# Part 1
# root = recursive_circus(tower)
# print root

# Part 2
# part_2(root)
