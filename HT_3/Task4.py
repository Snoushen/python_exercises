"""
4. Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат.
Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi, обробляє повернутий ними результат та також повертає результат.
Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3
"""
#
def function_1(function):
    return "Твоє" + function

def function_2(function):
    return " ім'я" + function

def function_3(string_name):
    return ", =  " + function

def function_4(name):
    answer_text = function_1(function_2(function_3(name)))
    return print(answer_text)

print("Як тебе звати?")
function_4(input())
