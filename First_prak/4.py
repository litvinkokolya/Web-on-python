def troika_pifagor():
    print("Введите два числа (диапазон): ")

    a = int(input())
    isInt(a)
    b = int(input())
    isInt(b)


    for i in range(a, b+1):
        for j in range(a, b+1):
            for f in range(a, b+1):
                if i*i+j*j == f*f:
                    print("{", i, ";", j, ";", f, "}")

def isInt(n):
    return int(n) == float(n)

troika_pifagor()