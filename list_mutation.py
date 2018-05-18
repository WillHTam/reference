# avoid mutating a list while iterating over it

list1 = [1, 2, 3, 4]
list2 = [1, 2, 5, 6]


def incorrect(arr1, arr2):
    for i in arr1:
        if i in arr2:
            arr1.remove(i)


incorrect(list1, list2)
# this generates a list1 of [2,3,4]
#    Python uses an internal counter to keep track of the index it is in the loop
#    mutating the list length does not automatically update the counter
#    => therefore the loop never sees element 2


# correct method
def remove_dupes(arr1, arr2):
    arr1_copy = arr1[:] # clone list first
    for i in arr1_copy:
        if i in arr2:
            arr1.remove(i)
