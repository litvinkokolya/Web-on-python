print("Диапазон: ")
a = int(input())
b = int(input())
guess = False
attempts = 0

while not guess:
    number = (a+b) // 2
    print("Я думаю это", number)
    answer = input(": ")
    if not answer in ("<", ">", "="):
        print("Ты не то ввёл")
        continue
    if answer == "<":
        b = number
    elif answer == ">":
        a = number
    else:
        guess = True
    attempts += 1
print("Отгадано за,", attempts, "попыток")