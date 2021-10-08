print('Введите длину первого прямоугольника')
try:
    a = int(input()) 
except ValueError: 
    print('Число должно быть целым и неотрицательным')
    exit()
print('Введите ширину первого прямоугольника')
try: 
    b = int(input())
except ValueError:
    print('Число должно быть целым и неотрицательным')
    exit()
print('Введите длину второго прямоугольника')
try: 
    c = int(input())
except ValueError:
    print('Число должно быть целым и неотрицательным')
    exit()
print('Введите длинну второго прямоугольника')
try:
    d = int(input())
except ValueError:
    print('Число должно быть целым и неотрицательным')
    exit()
if ((c-a)>=1 and (d-b)>=1) :print('Да')
else: 
    if ((c-d)>=1 and (d-a)>=1) :print('Да')
    else:  print('Нет')
