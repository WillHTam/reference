import random

def quicksort(array, left=0, right=-1):
    def swap(array, a, b):
        # helper function for swapping indices a and b
        array[a], array[b] = array[b], array[a]

    if right == -1:
        right = len(array)

    # base case
    if right-left <= 1:
        return

    pivot = random.randrange(left, right) # Generate pivot index
    i = left+1 # Barrier between below and above pivot, first higher element
    swap(array, left, pivot)

    for j in range(left+1,right):
        if array[j] < array[left]:
            swap(array, i, j)
            i = i+1

    swap(array, left, i-1) # i-1 is now the pivot
    quicksort(array, left, i-1)
    quicksort(array, i, right)

    return array


print( quicksort( [10, 5, 2, 69, 1, 3, 2]  ) )