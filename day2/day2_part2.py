f = open("day2_input.txt", 'r')
total_score = 0
for x in f.readlines():
    op_shape = x[0]
    outcome = x[2]
    if outcome == 'X':
        if op_shape == 'A':
            total_score += 3
        elif op_shape == 'B':
            total_score += 1
        elif op_shape == 'C':
            total_score += 2
    elif outcome == 'Y':
        total_score += 3
        if op_shape == 'A':
            total_score += 1
        elif op_shape == 'B':
            total_score += 2
        elif op_shape == 'C':
            total_score += 3
    elif outcome == 'Z':
        total_score += 6
        if op_shape == 'A':
            total_score += 2
        elif op_shape == 'B':
            total_score += 3
        elif op_shape == 'C':
            total_score += 1
print(total_score)