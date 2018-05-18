def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

print('\nIs "eve" a palindrome?')
print(isPalindrome('eve'))

print('\nIs "wombat" a palindrome?')
print(isPalindrome('wombat'))

print('\nIs "able was I ere I saw Elba" a palindrome?')
print(isPalindrome('Able was I, ere I saw Elba'))
