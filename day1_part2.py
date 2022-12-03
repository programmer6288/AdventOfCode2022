f = open("day1_input.txt", 'r')
cal_list = f.readlines()
elf_list = []
curr = 0
for x in cal_list:
    if x == '\n':
        elf_list.append(curr)
        curr = 0
    else:
        curr += int(x.strip())
elf_list.sort(reverse=True)
print(elf_list[0] + elf_list[1] + elf_list[2])