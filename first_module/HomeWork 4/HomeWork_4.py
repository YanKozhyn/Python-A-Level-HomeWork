def Task1():
    sum_of_list = 0
    sum_of_odd = 0
    sum_of_even = 0
    array = [0,1,2,3,23,321,5,6,7,321,9]
    for i in range(len(array)):
        if (i % 2 == 0):
            print(f"Number with even index: {array[i]}", end=', ')
        sum_of_list += array[i]
        if (array[i] % 2 == 0):
            sum_of_even += array[i]
        if (array[i] % 2 != 0):
            sum_of_odd += array[i]
    print("")
    print(f"Sum of all elements of list: {sum_of_list}")
    print(f"Sum of even elements of list: {sum_of_even}")
    print(f"Sum of odd elements of list: {sum_of_odd}")
    max_number = max(array)
    index_of_max_number = array.index(max_number)
    print(f"The biggest number is {max(array)} and index of this number {index_of_max_number}")

def Task2():
    with open('HomeWorks/file_1.txt') as f:
        lines = f.read().split()
        list_of_numbers = [eval(i) for i in lines]
        num_1 = list_of_numbers[0]
        num_2 = list_of_numbers[1]
        for i in range(len(list_of_numbers)):
            if (list_of_numbers[i] % num_1 == 0) and (list_of_numbers[i] % num_2 == 0):
                print('FB')
            elif list_of_numbers[i] % num_1 == 0:
                print('F')
            elif list_of_numbers[i] % num_2 == 0:
                print('B')
            else:
                print(list_of_numbers[i])

def Task3():
    new_list = []
    range_one_first = 0
    range_two_first = 5
    range_one_second  = 5
    range_two_second = 10
    list = [1,2,34,5,51,9,544,2,56,61,25,61,2,421,51,54,56,17,621,3213,4,21,421,41,24,1,5,1,34,2,1,54,551]
    dsad = len(list) // 5
    for i in range(dsad):
        new_list += sorted(list[range_one_first:range_two_first])
        range_one_first += 10
        range_two_first += 10
        new_list += sorted(list[range_one_second:range_two_second], reverse=True)
        range_one_second += 10
        range_two_second += 10
    print(f"Initial list {list}")
    print(f"Final list   {new_list}")

