def accumulate(objects):
    accumulator = objects[0]
    for idx, obj in enumerate(objects):
        yield accumulator
        if idx < len(objects) - 1:
            accumulator += objects[idx + 1]


for acc in accumulate(["ala ", "ma ", "kota "]):
    print(acc, end=" ")
