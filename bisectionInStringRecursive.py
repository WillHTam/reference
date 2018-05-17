def isIn(char, aStr):
  if len(aStr) > 1:        
      if char == aStr[len(aStr)//2]:
          return True
      elif char > aStr[len(aStr)//2]:
          return isIn(char, aStr[len(aStr)//2:])
      else:
          return isIn(char, aStr[:len(aStr)//2])         
  elif len(aStr) == 1:
      return char == aStr
  return False

def isInTwo(char, aStr):
  if len(aStr) <= 1:
      return char == aStr
  elif char >= aStr[len(aStr)//2]:
      return isIn(char, aStr[len(aStr)//2:])
  return isIn(char, aStr[:len(aStr)//2])

def isInThree(c, s): 
  return False if len(s) < 1 else \
    True if c == s[len(s) // 2] else \
    isInThree(c, s[: len(s) // 2]) if c > s[len(s) // 2] else \
    isInThree(c, s[len(s) // 2 :])

c = 'a'
s = 'abcdef'
print(isIn(c,s))
print(isInTwo(c,s))
print(isInThree(c,s))