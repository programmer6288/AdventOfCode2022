f = open("day1_input.txt", 'r')
cal_list = f.readlines()
max_cals = 0
curr = 0
for x in cal_list:
    if x == '\n':
        max_cals = max(curr, max_cals)
        curr = 0
    else:
        curr += int(x.strip())
print(max_cals)