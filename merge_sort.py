"""
Merge Sort
- Divide and conquer approach:
    1) if list is of length 0 or 1, already sorted
    2) if list has more than one element, split into two lists, and sort each
    3) merge sorted sublists
        - look at first element of each move smaller to end of the result\
        - when one list is empty, just copy the rest of other list\
        - merge such that sublists will be sorted until finished
            - keep splitting original list down until have lists of 1 elemen
            - then compare and merge back up  
- In many cases, will not take linear time as final append will happen before going through whole list

- Complexity
    - of the sublist merging
        - go through two lists, only one pass
        - compare only smallest elements in each sublist
        - O(len(left) + len(right)) elements
        - O(len(longer lists)) for comparisons
        - linear to length of lists
    - for merge sort
        - at first recursion level
            - n/2 elements in each list
            - O(n) + O(n) = O(n) where n is len(L)
    - at second recursion level
        - n/4 elements in each list
        - two merges => O(n) where n is len(L)
        - so just at this second level still going through the list
    - each recursion level is O(n) where n is len(L)
    - dividing list in half with each recursive call
        - O(log(n)) where n is len(L)
    - overall complexity is therefore O(n log(n)) where n is len(L)
        - loglinear is the fastest a search can be
"""

def merge(left, right):
    '''
    : performing sublist merge
    : given two sorted lists, look at first element and append
    : the lower to result.  if one list is empty, copy the remainder
    : of the other list to 
    '''
    result = []
    i, j = 0, 0 # indices of the walk down the lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i]) # add left if smaller
            i += 1 # move index up
        else:
            result.append(right[j]) # add right if smaller
            j += 1
    # when either list is exhausted move on to these
    # which just append the remainder to the end of result
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

def merge_sort(L):
    if len(L) < 2: # base case
        return L[:]
    else:
        middle = len(L)//2 # floor division
        # divide list successively into halves
        # depth-first such that conquer smallest pieces down one branch first
        # _before_ moving to larger pieces
        left = merge_sort(L[:middle]) # divide
        right = merge_sort(L[middle:]) # divide
        return merge(left, right) # conquer

i = [1,5,2,3,5,6,7,7,2,3,2,8]
print(merge_sort(i))
