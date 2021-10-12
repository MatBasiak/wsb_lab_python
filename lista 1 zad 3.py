def accumulate(objects):
    accumulator = objects[0]
    for inx, obj in enumerate(objects):
        yield accumulator
        if inx < len(objects) - 1:
            accumulator += objects[inx + 1]

for acc in accumulate(["ala ","ma"," kota"]):
    print(acc)