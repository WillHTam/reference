class Item():
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value) + ', '\
                 + str(self.weight) + '>'
        return result


def powerSet(items):
    """
    :param items: iterable
    :return: one subset, requiring 2**len(items) next calls
    """
    N = len(items)
    for i in range(2**N):
        combo = []
        for j in range(N):
            print('\n')
            print('current i:', i, 'current j:', j)
            if (i >> j) % 2 == 1:
                print('bitwise:', i >> j)
                print('true!')
                combo.append(items[j])
                print('combo:', combo)
        yield combo

def buildItems():
    """
    :return: list of defined Item objects
    """
    names = ['clock', 'painting', 'radio', 'vase', 'book',
             'computer']
    vals = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    return Items


def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.
      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    N = len(items)
    for i in range(3**N):
        bag1 = ''
        bag2 = ''
        for j in range(N):
            k = 3 ** j
            if (i // k) % 3 == 0:
                bag1 = items[j]
            elif (i // k) % 3 == 1:
                bag2 = items[j]
            else:
                pass
        yield bag1, bag2


items = buildItems()
combos = yieldAllCombos(items)
x = [combos.__next__() for _ in range(10)]
for f in x:
    print(f)
