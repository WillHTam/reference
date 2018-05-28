# Bisection Search
# finish looking through list when 1 = n/(2^i) => i = log n
# complexity is O(log n), where n is len(list)

def bisect_search(L, e):
    if L == []:
        return False
    elif len(L) -- 1:
        return L[0] == e
    else:
        half = len(L)//2
        if L(half) > e:
            return bisect_search( L[:half], e )
        else:
            return bisect_search( L[half:], e )
# we know the recursive calls are not constant, but more importantly
# they make copies of the lists which adds up to a larger complexity
# O(log n) bisect_search calls, and O(n) for each call to copy list in recursive bisect_search call
# result of O(n log n)

def bisect_two(L, e):
    # changing where the pointers go to
    def bisect_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: # nothing left to search
                return False
            else:
                return bisect_helper(L, e, low, mid-1) # change numbers instead of copying list
        else:
            return bisect_helper(L, e, mid+1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_helper(L, e, 0, len(L)-1)
# pass list and indices as parameters
# list never copied just re-passed, which results in O(log n)

# cost - bisection search must be applied on a sorted list
# when does it make sense to sort first then search?
# if SORT + O(log n) < O(n) => SORT < O(n) - O(log n)
# but sorting time being less than O(n) is never true

# so if just doing a search once, better to do linear search
# however, if doing multiple search, can _amortize_ cost of the sort over many searches
# ie one sort for many searches
# SORT + K*O(log n) < K*O(n) => for large K, SORT time becomes irrelevant