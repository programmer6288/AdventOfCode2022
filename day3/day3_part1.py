f = open("day3_input.txt", 'r')
total_priority = 0
for x in f.readlines():
    str1 = x[:len(x)//2]
    str2 = x[len(x)//2:]
    common_char = ''.join(set(str1).intersection(str2))
    priority = ord(common_char) - ord('A') + 27 if common_char.isupper() else ord(common_char) - ord('a') + 1
    total_priority += priority
print(total_priority)