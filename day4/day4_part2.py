f = open("day4_input.txt", 'r')
count = 0
for x in f.readlines():
    int_pair = x.split(',')
    start1, end1 = [int(a) for a in int_pair[0].split('-')]
    start2, end2 = [int(a) for a in int_pair[1].split('-')]
    if start1 <= start2 <= end1 or start2 <= start1 <= end2:
        count += 1
print(count)