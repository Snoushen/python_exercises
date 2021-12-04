"""
1. Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів.
   Після запуска програми на екран виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора.
   Кожну секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах.
   Приблизний результат роботи наступний:
      Red        Green
      Red        Green
      Red        Green
      Red        Green
      Yellow     Green
      Yellow     Green
      Green      Red
      Green      Red
      Green      Red
      Green      Red
      Yellow     Red
      Yellow     Red
      Red        Green
"""


import time

def traffic_light():
    lights = ["Red","Yellow","Green","Yellow"]
    while True:
        ped_cross = lights[2]
        for i in lights:
            x = 4
            if i == lights[2]:
                ped_cross = lights[0]
            if i == "Yellow":
                x = 2
            for y in range(x):
                time.sleep(1)
                print(f'{i:<10}',ped_cross)


traffic_light()


