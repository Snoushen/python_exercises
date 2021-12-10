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
from pathlib import Path

def strange_fun(filename,char):

    def print_symbol(start, stop, string):
        i = 0
        block = ""
        while i < len(string):
            if i == start:
                x = i + stop
                while i < x:
                    block += string[i]
                    i += 1
            i += 1

        return block

    outpath = Path.cwd() / filename

    with open(outpath,'r') as file:
        data_all_symbol = file.read()
        without_space = data_all_symbol.replace(" ","")

        if char > len(without_space):
            raise ValueError(f'Number of symbol in file {len(without_space)}, request = {char}')

        initial_index_middle = int((len(without_space) / 2)-char/2)

        print(without_space,"\n")

        first = print_symbol(0, char,without_space)
        second = print_symbol(initial_index_middle, char, without_space)
        third = print_symbol(len(without_space)-char, char,without_space)

        result = [first,second,third]

        print("")
        print(result)

symbol_in_block = int(input("Symbol in one block: "))
strange_fun("test1.txt",symbol_in_block)




