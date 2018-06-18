def fib(n):
    '''
    Very inefficient
    If each recursive call took a nanosecond, fib(120) would take about
    250,000 years to finish.
    Order of growth grows with fib(n)
    In the recursion tree, there are many calculations repeated
        And therefore memoization is good to apply
    
    Memoization:
    Create a table to record what we've done
        - Before computing fib(x), check if value of fib(x) already in table
            - If so, look it up
            - If not, compute and then add to table
    '''
    if n is 0 or n is 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(10))

def fast_fib(n, memo={}):
    """
    Assumes n is an int >= 0, memo only used by recursive calls
    Returns Fibonacci of n
    
    ~ When does Memoization work? ~
    - Optimal Substructure
        a globally optimal solution can be found by combining optimal solutions to
        local subproblems
        * For x > 1, fib(x) = fib(x - 1) + fib(x - 2)
    - Overlapping subproblems:
        finding an optimal solution involves solving the same problem multiple times
        * computing fib(x) 
    """
    if n is 0 or n is 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fast_fib(n-1, memo) +\
                fast_fib(n-2, memo)
        memo[n] = result
        return result

print(fast_fib(10))
for i in range(121):
    print('fib(' + str(i) + ') =', fast_fib(i))    
