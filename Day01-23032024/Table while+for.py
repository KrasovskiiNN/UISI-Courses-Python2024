# Вложенный цикл - пример: Таблица Умножения

i = 1
j = 1

while i < 10:
    while j < 10:
        for i in range(1,10,1):
            print(i * j, end="\t")

        j = j + 1



