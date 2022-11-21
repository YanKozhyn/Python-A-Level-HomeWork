def removespace(line):
    amount_of_spaces = line.count(' ', line.find(' '), line.rfind(' '))
    return print(line.replace(' ', '', amount_of_spaces))
