"""
2. Написати функцію < bank > , яка працює за наступною логікою: користувач робить вклад у розмірі < a >
одиниць строком на < years > років під < percents > відсотків (кожен рік сума вкладу збільшується на цей відсоток,
ці гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки).
Параметр < percents > є необов'язковим і має значення по замовчуванню < 10 > (10%).
Функція повинна принтануть і вернуть суму, яка буде на рахунку.
"""
import functools

def bank(money,years,percents=10):
    rich_bitch = functools.reduce(lambda a,b: a + b,[(money // 100) * percents for year in range(0, years)])
    return rich_bitch

input_money = int(input("How much money you would put? "))
input_years = int(input("For how much years? "))
input_percents = int(input("Percent in year: "))

print(bank(input_money,input_years,input_percents))