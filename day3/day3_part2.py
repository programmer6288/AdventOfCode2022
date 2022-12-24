f = open("day3_input.txt", 'r')
total_priority = 0
lines = f.readlines()
for i in range(0, len(lines), 3):
    str1 = lines[i]
    str2 = lines[i+1]
    str3 = lines[i+2]
    common_char = ''.join(set.intersection(set(str1), set(str2), set(str3)) - {'\n'})
    priority = ord(common_char) - ord('A') + 27 if common_char.isupper() else ord(common_char) - ord('a') + 1
    total_priority += priority
print(total_priority)

