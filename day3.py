import math

def spiral_memory(square):
    bottom_right_steps = int(math.ceil(math.sqrt(square)))
    bottom_right_steps = bottom_right_steps if bottom_right_steps % 2 != 0 else bottom_right_steps + 1
    print bottom_right_steps - (pow(bottom_right_steps, 2) - square) % (bottom_right_steps - 1) - 1

f = open('03_input.txt', 'r')
square = int(f.readline().strip())
spiral_memory(square)

    
