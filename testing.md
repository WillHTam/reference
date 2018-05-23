# Testing!

### Overview

1) ensure code runs
    => this will remove syntax and static semantic errors
2) have a set of expected of results
    => and so spot the places where there are errors

### Types of tests

- Unit Testing
    - Take each function/module and validate it separately
- Regression Testing
    - add test for bugs as you find them in a function
    - this will catch new/reintroduced errors 
- Integration Testing
    - Testing the overall program and the handoff of data
- Then you'll find you need to go back up the chain and fix

## Testing approaches

- Using intuition to come up with natural partitions
- Random Testing?

### Black Box Testing

- Explores all paths through the specification of the code
- designed without looking at the code

    ```py
    def sqrt(x, eps):
        """ 
        Assumes x, eps are floats, x>=0, eps>0 
        Returns res such that x-eps <= res*res <= x+eps
        """
        => Test with boundary(x=0), perfect square(x=5), less than 1, irrational roots, extremes
    ```
    - can be done by someone other than the implementer to avoid biases
    - paths through specification
        - applies to lists? perform on big, small, weird lists
        - applies to numbers? try big, small, ints, floats

    ```py
    def size(aSet):
    ```
    test suite would include
    an empty set, set of size 1, set of size greater than 1

    ```py
    def union(set1, set2):
        """
        set1 and set2 are collections of objects, each of which might be empty.
        Each set has no duplicates within itself, but there may be objects that
        are in both sets. Objects are assumed to be of the same type.

        This function returns one set containing all elements from
        both input sets, but with no duplicates.
        """
    ```
    - Black box test suite would be all of:
    - set1 is an empty set; set2 is an empty set
    - set1 is an empty set; set2 is of size greater than or equal to 1
    - set1 is of size greater than or equal to 1; set2 is an empty set
    - set1 and set2 are both nonempty sets which do not contain any objects in common
    - set1 and set2 are both nonempty sets which contain objects in common

### Glass Box Testing

- Explores all paths through the code itself
- uses code directly to guide design of test cases
- ideally have a test case for each path through the code
- 'path-complete' if every potential path is tested at least one
    - drawbacks: can go through loops arbitrary times, missing paths

- GUIDELINES

    - branches
        - exercise all parts of a conditional
    - for loops
        - loop not entered?
        - body of loop executed once or multiple times?
    - while loops
        - like for loop + catch all ways to exit loop

    ```py
    def abs(x):
        """
        assumes x is an int
        returns x if x>=0 and x otherwise
        """
        if x < -1:
            return -x
        else:
            return x
    ```
    - path-complete suite of (2,-2) misses error in abs(-1)
        => test boundaries

    ```py
    def maxOfThree(a,b,c) :
        """
        a, b, and c are numbers

        returns: the maximum of a, b, and c
        """
        if a > b:
            bigger = a

        else:
            bigger = b

        if c > bigger:
            bigger = c

        return bigger
    ```
    - 4 test cases of
        - (a<b)>c
        - (a>b)>c
        - (a>b)<c
        - (a<b)<c

    ```py
    def union(set1, set2):
        """
        set1 and set2 are collections of objects, each of which might be empty.
        Each set has no duplicates within itself, but there may be objects that
        are in both sets. Objects are assumed to be of the same type.

        This function returns one set containing all elements from
        both input sets, but with no duplicates.
        """
        if len(set1) == 0:
            return set2
        elif set1[0] in set2:
            return union(set1[1:], set2)
        else:
            return set1[0] + union(set1[1:], set2)
    ```

    test suite: union('','abc'), union('a','abc'), union('ab','abc'), union('d','abc')

    Since we are testing all possible paths:
        - should contain tests that test when set1 is empty, when set1[0] is in set2, and when set1[0] is not in set2
        -  The test suite should also test when the recursion depth is 0, 1, and greater than 1.

    - len(set1) == 0 - matched by the test union('', 'abc')
    - set1[0] in set2 - matched by the test union('a', 'abc')
    - set1[0] not in set2 (this is the else: of the conditional) - matched by the test union('d', 'abc')

    In addition, because union is a recursive function, we should make sure our test set considers a recursion depth of 0, 1, and many. In this case, recursion depth is covered by some of the tests we've already chosen:
    - Recursion depth = 0 - matched by the test union('', 'abc')
    - Recursion depth = 1 - matched by the tests union('a', 'abc'), union('d', 'abc')
    - Recursion depth > 1 - matched by the test union('ab', 'abc')

    ```py
    def foo(x, a):
        """
        x: a positive integer argument
        a: a positive integer argument

        returns an integer
        """
        count = 0
        while x >= a:
            count += 1
            x = x - a
        return count
    ```
    - test suite would cover not running, running once, running multiple times

##　虫
- Isolate
- Attempt to fix
- Retest

- Overt vs Covert
    - Overt - obvious manifestation of crash or runs forever
    - Covert - no obvious manifestation, successful return of a value of which may be hard to determine validity

- Persistent vs intermittent
    - Persistent occurs every time code is run
    - Intermittent only occurs some times, even if run on same input
        - perhaps a result of time dependency

- Overt and persistent is a goal of defensive progamming
    - making bugs fall into this category makes them easy to detect

- Overt and intermittent - harder but can be handled if conditions can be reproduced

- Covert - highly dangerous because may not realize code is wrong until it has been run for a long time

- Ask how, not what did I do wrong
    - Is it part of a family of problems that I need to solve?

- print() out to test hypotheses
    - at enter function
    - parameters
    - function results

### bisection method
- print out halfway to see where bug might be occuring

### Don't vs Do
- Don't
    - Write entire program
    - Test entire program
    - Debug entire program
- Do
    - Write a functino
    - Test and debug function
    - Repeat with modules and then perform integration testing
- Don't
    - Change code
    - Remember where bug was
    - Test code
    - Forget where bug was or what change was made
    - Panic
- Do
    - Backup code
    - Change code
    - Write down potential bug in a comment
    - Test code
    - Compare new version with old version

### Assertions

- raise an AssertionError by throwing an error if the output does not what was expected
- stop immediately if the assertion is not met

```py
    def avg(grades):
        """
        raises AssertionError if given an empty string for grades
        uses 'no grades data' as the string to print out
        otherwise continues 
        """
        assert not len(grades) == 0, 'no grades data'
        return sum(grades) / len(grades)
```

- assertions don't allow a programmer to control response to unexpected conditions
- ensure that execution halts whenever an unexpected condition is not met
- typically used to check inputs to functions procedures, but can be used anywhre
- can be used to check outputs of a function to avoid propagating bad values

- Where to use assertions?
    - supplement to testing
    - raise exceptions if users supply bad data input
    - use assertions to
        - check types of arguments or values
        - check that invariants on data structures are met
            - is this a list of more than one element?
        - check constraints on return values
        - check for violations of constraints on procedure (eg no duplicates in a list)
