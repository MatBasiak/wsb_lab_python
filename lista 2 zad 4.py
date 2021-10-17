class Odd_first:
    def __init__(self, objects):
        self.object = objects
        self.odd = objects[1::2]
        self.even = objects[::2]
        self.sorted_object = [*self.even, *self.odd]
        self.counter = -1

    def __next__(self):
        self.counter += 1
        if self.counter <= len(self.sorted_object) - 1:
            return self.sorted_object[self.counter]
        else:
            raise StopIteration

    def __iter__(self):
        return self


odd_first = Odd_first(["A", "B", "C", "D", "E"])

for x in odd_first:
    print(x, end=" ")
