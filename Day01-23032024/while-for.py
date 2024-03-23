number = 3
while number < 5:
    print(number)
    number = number + 1
print("The End")

'''
ИТЕРАЦИЯ (один цикл):
print(number)
number = number + 1
'''

number2 = 24
while number2 > 20:
    print(number2)
    number2 -= 1
print("The End 2")

#  Функция range()

for n in range(10):
    print(n, end=" ")
else:
    print("Exit")

# Вложенный цикл - пример: Таблица Умножения

i = 1
j = 1

while i < 10:
    while j < 10:
        print(i*j, end="\t")
        i = i+1

    j = 1
    i = i + 1