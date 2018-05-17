def gcdIter(a, b):
  smaller = min(a, b)
  
  iterable = list(range(1, smaller+1))[::-1]
    
  for i in iterable:
    if (a % i == 0 ) and ( b % i == 0):
      return i
    
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
      return a
    else:
      return gcdRecur(b, a % b)
    

print( gcdRecur(10, 15) == gcdIter(10, 15) )
