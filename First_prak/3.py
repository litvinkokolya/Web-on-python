i = int(input("Введите натуральное число: "))
ls = []
while i > 0:
    ls.append(i % 10)
    i //= 10

r = max(ls)
print("Максимальный элемент:", r)
ls.reverse()
print(ls)

end_ls = []

for f in range(len(ls)):
    end_ls.append(ls[f])

for f in range(len(ls)):
    if ls[f] == r:
        end_ls.insert(f+1,r)

print(end_ls)

