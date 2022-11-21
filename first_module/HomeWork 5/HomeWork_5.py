def sorted_list(list, start, end):
    list[start:end] = sorted(list[start:end])
    print(list)
    pass
list = [1,10,9,4,5,7,2,0]
start = 2
end = 6
sorted_list(list, start, end)

def math_calculation(file):
    with open(file, 'r+') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            new_lines = lines[i].replace("\n", "")
            try:
                f.write(f"{new_lines} = {eval(new_lines)} \n")
            except (ZeroDivisionError):
                f.write(f"{new_lines} = can not division by zero \n")
    pass
math_calculation('HomeWorks/file_1.txt')

def check_palindrom(word):
   new_word = ''.join(item for item in word if item.isalnum())
   if (new_word == new_word[::-1]):
       print(f"Word: {new_word} is Palindrome")
   else:
       print(f"Word: {new_word} is not Palindrome")
   pass
str = "12_.2?1"
check_palindrom(str)