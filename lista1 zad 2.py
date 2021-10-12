def repeat(obj, *args):
    print(args[0])
    if args and args[0] != None:
        for i in range(0, args[0]):
            yield obj
    else:
        while True:
            yield obj


for object in repeat(5, None):
    print(object)