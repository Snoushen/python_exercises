"""
2. Написати функцію < bank > , яка працює за наступною логікою: користувач робить вклад у розмірі < a >
одиниць строком на < years > років під < percents > відсотків (кожен рік сума вкладу збільшується на цей відсоток,
ці гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки).
Параметр < percents > є необов'язковим і має значення по замовчуванню < 10 > (10%).
Функція повинна принтануть і вернуть суму, яка буде на рахунку.


"""
import functools
def bank(money,years,percents=10):

    iban = money

    for i in range(0,years):
        print(iban)
        iban = (iban / 100) * percents + iban

    return iban

input_money = int(input("How much money you would put? "))
input_years = int(input("For how much years? "))


print(bank(input_money,input_years))
