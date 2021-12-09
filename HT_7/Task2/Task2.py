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

def strange_fun(filename,char):
    with open(f'{filename}.txt','r') as file:
        data_all_symbol = file.read()
        without_space = data_all_symbol.replace(" ","")

        if char > len(without_space):
            raise ValueError(f'Number of symbol in file {len(without_space)}, request = {char}')
        my_string = without_space[:char]

        middle_index = int((len(my_string) /2)-(3/2))

        middle2 = int(len(my_string) / 2)
        print(my_string,end="")
        print("\n", (middle2 - 1) * " " + "^")
        for i in range(len(my_string)):
            if len(my_string) % 2 == 0:
                if i <= 2:
                    print(my_string[i],end="")
                elif middle_index < i <= middle_index+3:
                    print(my_string[i],end="")
                elif i > len(my_string)-4:
                    print(my_string[i],end="")
                else:
                    print(" ",end="")
            if len(my_string) % 2 != 0:
                if i <= 2:
                    print(my_string[i], end="")
                elif middle_index-1< i <= middle_index + 2:
                    print(my_string[i], end="")
                elif i > len(my_string) - 4:
                    print(my_string[i], end="")
                else:
                    print(" ", end="")
        print("\n",(middle2 - 1) * " " + "^")

strange_fun("test1",12)
print(30*"=")
strange_fun("test2",25)
print(30*"=")
strange_fun("test3",3)


