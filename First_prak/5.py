import random
from random import randint

random_number = randint(1,5)
m = "мармеладка"
forms = ["квадратная", "мишка", "программист", "овальная", "круглая"]

class Switch:
    def __init__(self, value):
        self.value = value

    def case(self, value, code):
        if self.value == value:
            code()
        return self


def value_1():
    print('апельсиновая', m, random.choice(forms) )


def value_2():
    print('острая', m, random.choice(forms))


def value_3():
    print('яблочная', m, random.choice(forms))

def value_4():
    print('кокосовая...', m, random.choice(forms))

def value_5():
    print('лимонная', m, random.choice(forms))

Switch(random_number) \
    .case(1, lambda: value_1()) \
    .case(2, lambda: value_2()) \
    .case(3, lambda: value_3()) \
    .case(4, lambda: value_4()) \
    .case(5, lambda: value_5())

#Знаю, что задачу можно сделать намного проще без функций и класса (например, как я тут же сделал через список...),
#но почему то изначально вспомнилось о кейсах из плюсов