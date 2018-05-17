def iterPower(base, exp):
    count = exp
    last = 1
    for _ in range(exp):
      last *= base
      count -= 1
    return last

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 1:
        return base
    elif exp == 0:
        return 1
    else:
        return base * iterPower(base, exp - 1)

print( iterPower(2,3) == recurPower(2,3) )
