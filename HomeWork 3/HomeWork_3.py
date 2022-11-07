

def Task1():
    word = input("Enter some words: ")
    print(word[(len(word)-1)//2:(len(word)+2)//2])

def Task2():
    data = input("Enter word from 5 to 15 chars: ")
    if (len(data) >= 5 and len(data) <= 15):
        part_1 = (data[len(data) // 2:])
        part_2 = (data[:len(data) // 2])
        part_2_upper = part_2.upper()[len(part_2) - 3 : len(part_2)]
        print(part_1 + part_2[:len(part_2) - 3] + part_2_upper)
    else:
        print("Wrong input. Please enter word from 5 to 15 chars")

def Task3():
    word = input("Enter word to 10 chars: ")
    if (len(word) <= 10):
        word_with_small_chars = word[-3:].lower()
        new_word = word[:-3]
        print(new_word[:2] + word_with_small_chars + new_word[2:])
    else:
        print("Wrong input. Please enter word to 10 chars!!!")

def Task4():
    range_square = int(input("Enter which square you want: "))
    for i in range(range_square):
        for j in range(range_square):
            if (i == 0 or i == range_square - 1 or j == 0 or j == range_square - 1):
                print("#", end="")
            else:
                print(" ", end="")
        print()