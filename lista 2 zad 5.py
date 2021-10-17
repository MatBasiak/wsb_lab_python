class Chain:

    def __init__(self, *args):
        self.flatten_args = []
        for arg in args:
            for arg_element in arg:
                self.flatten_args.append(arg_element)
        self.counter = -1

    def __next__(self):
        self.counter += 1
        if self.counter <= len(self.flatten_args) - 1:
            return self.flatten_args[self.counter]
        else:
            raise StopIteration

    def __iter__(self):
        return self


# chain = Chain('ABC', 'DEF')
# chain = Chain([1, 2, 3], [4, 5, 6], [7, 8, 9])
chain = Chain("ABC", [1, 2, 3], [], "DEF")

for char in chain:
    print(char, end=" ")
