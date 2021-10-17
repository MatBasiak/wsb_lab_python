class Tetranacci:

    def __init__(self, steps):
        self.steps = steps
        self.counter = 0
        self.a, self.b, self.c, self.d, self.e = 0, 0, 0, 1, 1
        self.n

    def __next__(self):
        if self.counter < self.steps:
            self.counter += 1
            if self.counter in (1, 2, 3):
                return self.a
            elif self.counter in (4, 5):
                return self.d
            else:
                pass
        else:
            raise StopIteration

    def __iter__(self):
        return self


number = int(input("Podaj liczbę elementów do wyświeltenia: "))

tetra = Tetranacci(number)

for x in tetra:
    print(x, end=" ")
