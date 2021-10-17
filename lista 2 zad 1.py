class Count:

    def __init__(self, begin):
        self.begin = begin

    def __next__(self):
        self.begin += 1
        return self.begin

    def __iter__(self):
        return self


start = int(input("Podaj liczbę początkową: "))

count = Count(start)

for x in count:
    print(x, end=" ")
