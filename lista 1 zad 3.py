def accumulate(objects):
    if type(objects[0]) == str:
        accumulator = objects[0]
        for idx, obj in enumerate(objects):
            yield "'" + accumulator + "'"
            if idx < len(objects) - 1:
                accumulator += objects[idx + 1]

    else:
        accumulator = objects[0]
        for idx, obj in enumerate(objects):
            yield accumulator
            if idx < len(objects) - 1:
                accumulator += objects[idx + 1]


for acc in accumulate(["ala ", "ma", " kota"]):
        print(acc, end=", ")

print("\n")
for acc in accumulate([1, 2, 3, 4, 5]):
    print(acc, end=" ")
