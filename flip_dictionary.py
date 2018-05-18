# return new dictionary that flips keys and values of old dictionary
# new values should be sorted lists
# if the original dictionary had duplicate values, append the matching key to the list of the new dictionary, ie {1: True, 0:True} => {True: [0,1]}

def flip(d):
    new = {}
    for k in d.values():
        if k not in new.keys():
            new[k] = []    
    for k,v in d.items():
        new[v].append(k)
    for k,v in new.items():
        new[k] = sorted(v)
    return new

def flip2(d):
    new = {}
    for k in d.keys():
        if d[k] in new:
            new[d[k]].append(k)
        else:
            new[d[k]] = k
    for v in new.values():
        v.sort()
    return new

import bisect
def flippa(d):
    new = {}
    for k, v in d.items():
        bisect.insort(new.setdefault(v, []), k)
    return new
