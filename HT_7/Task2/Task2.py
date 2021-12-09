"""
2. Написати функцію, яка приймає два параметри: ім'я файлу та кількість символів.
   На екран повинен вивестись список із трьома блоками - символи з початку, із середини та з кінця файлу.
   Кількість символів в блоках - та, яка введена в другому параметрі.
   Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша, ніж є в файлі
(наприклад, файл із двох символів і треба вивести по одному символу, то що виводити на місці середнього блоку символів?)
   В репозиторій додайте і ті файли, по яким робили тести.
   Як визначати середину файлу (з якої брать необхідні символи) - кількість символів поділити навпіл, а отримане "вікно"
символів відцентрувати щодо середини файла і взяти необхідну кількість. В разі необхідності заокруглення одного чи обох параметрів - дивіться на свій розсуд.
"""

import os

def middle(some_string):
    middle_index = int((len(some_string) / 2))
    for x in range(len(some_string)):
        if x == middle_index:
            print("^")
        elif x < middle_index:
            print(" ", end="")
    return None

def strange_fun(filename,char):
    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)

    with open(f'{filename}','r') as file:
        data_all_symbol = file.read()
        without_space = data_all_symbol.replace(" ","")

        if char > len(without_space):
            raise ValueError(f'Number of symbol in file {len(without_space)}, request = {char}')
        my_string = without_space[:char]
        middle_index = int((len(my_string) / 2))

        print(my_string)
        middle(my_string)

        for i in range(len(my_string)):
            if i <= 2:
                print(my_string[i],end="")
            elif middle_index - 2 < i <= middle_index+1:
                print(my_string[i],end="")
            elif i > len(my_string)-4:
                print(my_string[i],end="")
            else:
                print(" ",end="")
        print("")
        middle(my_string)



strange_fun("test1.txt",1)
print(30*"=")
strange_fun("test2.txt",25)
print(30*"=")
strange_fun("test3.txt",3)
