import math

def spiral_memory(square):
    bottom_right_steps = int(math.ceil(math.sqrt(square)))
    bottom_right_steps = bottom_right_steps if bottom_right_steps % 2 != 0 else bottom_right_steps + 1
    print bottom_right_steps - (pow(bottom_right_steps, 2) - square) % (bottom_right_steps - 1) - 1

def part_2(square):
    n = 100 
    start =[[0 for i in range(n)] for j in range(n)] 
    start[n / 2][n / 2] = 1
    origin = n / 2
    i = 0
    while i < n:
        width = 8 * (i + 1) / 4
        for side in range(4):
            for position in range(width):
                sum = 0
                if side == 0:
                    sum = sum_of_adjacent_blocks(origin + i - position, origin + i + 1, start)
                    start[origin + i - position][origin + i + 1] = sum
                elif side == 1:
                    sum = sum_of_adjacent_blocks(origin - i - 1, origin + i - position, start)
                    start[origin - i - 1][origin + i - position] = sum
                elif side == 2:
                    sum = sum_of_adjacent_blocks(origin - i + position, origin - i - 1, start)
                    start[origin - i + position][origin - i - 1] = sum 
                elif side == 3:
                    sum = sum_of_adjacent_blocks(origin + i + 1, origin - i + position, start)
                    start[origin + i + 1][origin - i + position] = sum 
                if sum > square:
                    return sum

        i += 1
    
def sum_of_adjacent_blocks(row, col, start):
    return (start[row + 1][col - 1] + start[row + 1][col] + start[row + 1][col + 1] +
            start[row][col - 1] + start[row][col + 1] +
            start[row - 1][col - 1] + start[row - 1][col] + start[row - 1][col + 1])

f = open('03_input.txt', 'r')
square = int(f.readline().strip())

# Part 1
# spiral_memory(square)

# Part 2
# print(part_2(square))
