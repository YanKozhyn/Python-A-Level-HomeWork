def Task1():
    _year = int(input("Enter a year: "))
    if (_year % 400 == 0) and (_year % 100 == 0):
        print("YES")
    elif (_year % 4 == 0) and (_year % 100 != 0):
        print("YES")
    else:
        print("NO")

def Task2():
    _year = int(input("Enter a year: "))
    if not((_year % 400 == 0) ^ (_year % 100 == 0)):
        print("YES")
    elif not((_year % 4 == 0) ^ (_year % 100 != 0)):
        print("YES")
    else:
        print("NO")

def Task3():
    number_1 = int(input("Dear user, enter first number: "))
    number_2 = int(input("Dear user, enter second number: "))
    number_3 = int(input("Dear user, enter third number: "))
    for i in range(1, number_3 + 1):
        if (i % number_1 == 0) and (i % number_2 == 0):
            print('FB')
        elif i % number_1 == 0:
            print('F')
        elif i % number_2 == 0:
            print('B')
        else:
            print(i)