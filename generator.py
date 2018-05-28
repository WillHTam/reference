def gen():
    x = 0
    while True:
        yield x
        x += 1


g1 = gen()
lst = [g1.__next__() for i in range(11)]
print(lst)


def gen_primes():
    i = 1
    primes = []
    while True:
        hold = False
        i += 1
        for p in primes:
            if i % p == 0:
                hold = True
        if hold is False:
            primes.append(i)
            yield i


def gen_primer():
    i = 1
    primes = []
    while True:
        i += 1
        if all((i % p != 0) for p in primes):
            primes.append(i)
            yield i


primer = gen_primes()
print(primer.__next__())
print(primer.__next__())
print(primer.__next__())
print(primer.__next__())
