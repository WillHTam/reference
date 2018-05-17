
def findSmallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range( 1, len(array) ):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index

def selectionSort(array):
    hold = []
    for i in range(len(array)):
        smallest = findSmallest(array)
        hold.append(array.pop(smallest))
    return hold

print( selectionSort( [10, 5, 2, 69, 1, 3, 2]  ) )