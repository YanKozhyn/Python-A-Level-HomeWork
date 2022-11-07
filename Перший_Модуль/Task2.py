line = input("Print string: ")
upper_ctr, lower_ctr, number_ctr, special_ctr = 0, 0, 0, 0
for i in range(len(line)):
    if 'A' <= line[i] <= 'Z':
        upper_ctr += 1
    elif 'a' <= line[i] <= 'z':
        lower_ctr += 1
    elif '0' <= line[i] <= '9':
        number_ctr += 1
    else:
        special_ctr += 1
print([upper_ctr, lower_ctr, number_ctr, special_ctr])