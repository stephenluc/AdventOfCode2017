def inverse_captcha(digits):
    i = 0
    sum = 0
    while i < len(digits):
        if digits[i] == digits[(i + 1) % len(digits)]:
            sum += int(digits[i])
        i += 1
    print sum

def part_2(digits):
    i = 0
    sum = 0
    while i < len(digits):
        if digits[i] == digits[(i + len(digits) / 2) % len(digits)]:
            sum += int(digits[i])
        i += 1
    print sum

f = open('01_input.txt', 'r')
sequence = f.readline()

# Part 1
# inverse_captcha(sequence)

# Part 2
# part_2(sequence)
