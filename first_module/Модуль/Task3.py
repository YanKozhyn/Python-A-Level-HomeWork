line = input("Enter your string: ")
list = []
for i in range(len(line)):
    if line[i].isdigit():
        list.append(int(line[i]))
print(list)
