def even(x):
    if x%2==0:
        print(x)
    while True:
        x+=1
        if x % 2 == 0:
            yield x
        else:
            continue

for i in even(0):
    print(i)