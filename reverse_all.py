# reverse iterable, and reverse any iterables inside those
# ([0,1], (3,4)) =>  ((4,3), [1,0])

def reverse_all(L):
    clone = L[::-1]
    for i in clone:
        try:
            reverse_all(i)
        except:
            pass
    L[:] = clone

def reverse_all_two(L):
    hold = list(reversed(L))
    for i in hold:
        hold[ hold.index(i) ] = list(reversed(i))
    L[:] = hold
