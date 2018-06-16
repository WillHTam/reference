"""
https://books.google.com.hk/books?id=NLngYyWFl_YC&pg=PA127&dq=introduction+to+algorithm+heap+sort&hl=zh-CN&sa=X&ei=HnnTULG2Ga6QiAfhyoEQ#v=onepage&q=introduction%20to%20algorithm%20heap%20sort&f=false
"""
import heapq


def swap(i, j):
    """
    Swap two values helper function
    """                    
    sqc[i], sqc[j] = sqc[j], sqc[i] 


def heapify(end,i):   
    """
    create heap
    """
    l=2 * i + 1  
    r=2 * (i + 1)   
    max=i   
    if l < end and sqc[i] < sqc[l]:   
        max = l   
    if r < end and sqc[max] < sqc[r]:   
        max = r   
    if max != i:   
        swap(i, max)   
        heapify(end, max)   


def heap_sort():
    end = len(sqc)   
    start = end // 2 - 1 # use // instead of /
    for i in range(start, -1, -1):   
        heapify(end, i)   
    for i in range(end-1, 0, -1):   
        swap(i, 0)   
        heapify(i, 0)   


sqc = [1,3,3,5,4,2]
heap_sort()
print(1, sqc)


def heap_sorter(L):
    """
    Python built-in
    """
    h = []
    for value in L:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]


print(2, heap_sorter([1,3,3,5,4,2]))



