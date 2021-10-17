def even(x=None):
    if x is None:
        x = -1
    while True:
        x += 1
        if x % 2 == 0:
            yield x
        else:
            continue

# for i in even():
#     print(i, end=" ")


start = int(input("podaj liczbę od której zcząć: "))
for i in even(start):
    print(i, end=" ")
