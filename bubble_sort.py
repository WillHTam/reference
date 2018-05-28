# Bubble Sort
# compare consecutive pairs of elements
# swap elements in pairs such that smaller is first
# at end of list, do so again. stop when no more swaps have been made

def bubble_sort(L):
    """
    inner for loop does the comparisons
    outer while loop is doing multiple passes until no more swaps
    """
    swap = False # flag for indicating when finished
    while not swap:
        swap = True
        print(L)
        for i in range(1, len(L)):
            if L[i - 1] > L[i]: # if element is out of order, swap and set flag back to False
                swap = False
                temp = L[i]
                L[i] = L[i - 1]
                L[i - 1] = temp

# worst case? O(len(L)) for going through the whole list in the inner loop
# and through the whole list O(len(L)) for the while loop
# results in O(n*2) complexity where n is len(L)
# to do len(L) - 1 comparisons and len(L) - 1 passes

def bubble_two(L):
    last_index = len(L) - 1
    while last_index > 0:
        print(L)
        for i in range(last_index):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
        last_index -= 1
    return L


l = [1, 5, 3, 8, 4, 9, 6, 2]
m = l[:]
bubble_sort(l)
print('~')
bubble_two(m)
