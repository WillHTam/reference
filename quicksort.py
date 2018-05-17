
def quicksort(array):
    if len(array) < 2: # arrays with length of 0 /1 are already 'sorted'
        return array
    else:
        pivot = array[0] # recursive case

        less = [ i for i in array[1:] if i <= pivot ] # sub-array of all elements less than the pivot

        greater = [ i for i in array[1:] if i > pivot ] # sub-array of all the elements greater than the pivot

        return quicksort(less) + [pivot] + quicksort(greater)

print( quicksort( [10, 5, 2, 69, 1, 3, 2] ) )