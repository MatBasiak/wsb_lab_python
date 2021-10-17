class Tetranacci:

    def __init__(self, steps):
        self.steps = steps
        self.counter = -1
        self.tetranaci = [0, 0, 0, 1, 1]

    def __next__(self):
        self.counter += 1

        for i in range(5, self.steps + 1):
            self.tetranaci.append(
                self.tetranaci[i - 1] + self.tetranaci[i - 2] + self.tetranaci[i - 3] + self.tetranaci[i - 4])

        if self.counter == self.steps:
            raise StopIteration

        return self.tetranaci[self.counter]

    def __iter__(self):
        return self


number = int(input("Podaj liczbę elementów do wyświeltenia: "))

tetra = Tetranacci(number)

for x in tetra:
    print(x, end=" ")
