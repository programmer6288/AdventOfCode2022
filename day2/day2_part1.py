f = open("day2_input.txt", 'r')
total_score = 0
for x in f.readlines():
    op_shape = x[0]
    shape = x[2]
    if op_shape == 'A':
        if shape == 'X':
            total_score += 4
        elif shape == 'Y':
            total_score += 8
        elif shape == 'Z':
            total_score += 3
    elif op_shape == 'B':
        if shape == 'X':
            total_score += 1
        elif shape == 'Y':
            total_score += 5
        elif shape == 'Z':
            total_score += 9
    elif op_shape == 'C':
        if shape == 'X':
            total_score += 7
        elif shape == 'Y':
            total_score += 2
        elif shape == 'Z':
            total_score += 6
print(total_score)

