'''
На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.
'''
import random
n = int(input('введите количество монет: '))
brosok =list()
count_zero = 0
count_one = 0

for i in range (n):
    brosok.append(random.randint(0,1))
    if brosok[i]==0:
        count_zero += 1
    else:
        count_one += 1
print('монеты выпали следующим образом:')
print(brosok)
if count_one > count_zero:
    print(f'"орлов" нужно перевернуть {count_zero} шт.')
else:
    print(f'"решек" нужно перевернуть {count_one} шт.')