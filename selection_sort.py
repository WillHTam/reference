"""
Selection Sort
- first step
    - extract minimum element
    - swap with element at index 0
- next
    - in remaining sublist, extract minimum elemnt
    - swap with the element at index 1
- keep the left portion of the list sorted
    - at ith step, first i elements in list are sorted
    - all other elements are bigger than first i elements
- with bubble sort, there was a lot of percolation of elements
- selection sort goes in the other way.

- is there a loop invariant, is there a property that will hold true at each stage of this algorithm?
    - given prefix of list: L[0:i] and suffix: L[i+1 : len(L)]
    - then prefix is sorted and no element in prefix is larger than smallest element in suffic
    1) base case: prefix empty: suffix whole list - invariant true
    2) induction step: move minimum element from suffix to end of prefix. Since invariant true before move
        prefix sorted after append
    3) when exit, prefix is entire list, suffix empty, and therefore sorted

- Complexity
    - outer loop executes len(L) times
    - inner loop executes len(L) - i times
    - therefore, Quadratic complexity O(n^2) where n is len(L)
"""
def selection_sort(L):
    suffix_store = 0
    while suffix_store != len(L):
        print(L)
        # finding the right pointer, and insert at that spot
        for i in range(suffix_store, len(L)): # ranging from point to end of list...
            if L[i] < L[suffix_store]: # if current i is less than end of suffix...
                L[suffix_store], L[i] = L[i], L[suffix_store] # perform tuple swap between them
        suffix_store += 1 # increase index by one and move on

l = [1, 5, 3, 8, 4, 9, 6, 2]
selection_sort(l)
print('final: ',l)


def sel_sort(L):
    for i in range(len(L) - 1):
        print(L)
        minIndex = 1
        minVal = L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIndex = j
                minVal = L[j]
            j += 1
        temp = L[i]
        L[i] = L[minIndex]
        L[minIndex] = temp
