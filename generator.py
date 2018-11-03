def generator():
    x = 0
    while True:
        x += 1
        yield x

for i in generator():
    print(i)
    if i > 4:
        break


