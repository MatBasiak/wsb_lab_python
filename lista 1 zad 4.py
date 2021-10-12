def xrange(start, *end):
    if len(end) > 0:
        begin = start
        while begin < end[0]:
            yield begin
            begin += 1
    else:
        begin = 0
        while begin < start:
            yield begin
            begin += 1


for num in xrange(5,10):
    print(num)