class Repeat:
    def __init__(self, elem, times=None):
        self.elem = elem
        self.times = times
        self.counter = 0

    def __next__(self):
        if self.times is None:
            while True:
                return self.elem
        else:
            while self.counter < self.times:
                self.counter += 1
                return self.elem
            raise StopIteration

    def __iter__(self):
        return self


# repeat = Repeat(10, 3)
# repeat = Repeat(10, 5)
# repeat = Repeat(5)
repeat = Repeat(5, None)

for x in repeat:
    print(x, end=" ")
