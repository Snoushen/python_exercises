"""
5. Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями (дублікати значень - видалити). Словник для
   роботи захардкодити свій.
                Приклад словника (не використовувати):
                {'a': 1, 'b': 3, 'c': 1, 'd': 5}
                Очікуваний результат:
                {'a': 1, 'b': 3, 'd': 5}
"""
dict_double_value = {'a': 1, 'b': 1, 'c': 3, 'd': 3, 'e': ['ololo'], 'f' : ['ololo'], 'g' : ['ololo','lalala','elele']}

result = {}
print(dict_double_value)

for key,value in dict_double_value.items():
    if value not in result.values():
        result[key] = value




print(result)
