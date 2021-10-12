def even(x):
    if x % 2 == 0:
        print(x, end=" ")
    while True:
        x += 1
        if x % 2 == 0:
            yield x
        else:
            continue


for i in even(9):
    print(i, end=" ")
