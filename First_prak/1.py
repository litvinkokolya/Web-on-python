from random import randint
print("Выберите диапазон из 2 цифр(a,b)\n")
a = int(input())
b = int(input())
n = randint(a,b)
f = randint(1,5)
attempts = int(input("Введи количество попыток: "))
number = int(input("Ну давай, я загадал число. Тебе нужно его отгадать. Пиши: "))
i = 1
while i < attempts:
    if number > n:
        number = int(input("Бери меньше. Пробуй еще: "))
        if number > n:
            print("Бери еще меньше. Давай я тебе покажу примерную разницу: ", abs(number - n - f))
        elif number < n:
            print("Теперь бери больше. Давай я тебе покажу примерную разницу: ", abs(number - n - f))
        else:
            print("Ну ты угадал, вот число", n)
    elif number < n:
        number = int(input("Бери больше. Пробуй еще: "))
        if number < n:
            print("Бери еще больше, ты ошибся. Давай я тебе покажу примерную разницу: ", abs(number - n - f))
        elif number > n:
            print("Теперь бери меньше, ты опять ошибся! давай я тебе покажу примерную разницу", abs(number - n - f))
        else:
            print("Ну ты угадал, вот число", n)
    else:
        print("Ты угадал с", i, "попытки число", n)
        break
    i += 1
    if i == attempts:
        print("Game over koroche... Загаданное число: ", n)
