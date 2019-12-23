'''
NON-ORDERED list
element         +   -   +/-
is              1   n   n/2
no              n   n   n
'''
def non_ordered_linear_search(lst, key):
    for idx, item in enumerate(lst):
        if key == item:
            return idx
    return -1

testlist = [1, 2, 43, 55, 8, 90, 0, 61]
print(non_ordered_linear_search(testlist, 90))

'''
ORDERED list
element         +   -   +/-
is              1   n   n/2
no              n   n   n/2
'''
def ordered_linear_search(lst, key):
    for idx, item in enumerate(lst):
        if key == item:
            return idx
        elif item > key:
            return -1
        return -1

testlist = testlist.sort()
print(ordered_linear_search(testlist, 90))

'''
binary search
pre-ORDERED list!!!
element         +       -       +/-
is              1       log n   log n
no              log n   log n   log n
'''
def binary_search(lst, key):
    first = 0
    last = len(lst)-1

    while first <= last:
        mid = (first+last)//2
        if lst[mid] == key:
            return mid
        else:
            if key < lst[mid]:
                last = mid-1
            else:
                first = mid+1
    return -1

'''
element         +       -       +/-
is              1       log n   log n
no              log n   log n   log n
'''
def binary_search_with_recursion(lst, key):
    if len(lst) == 0:
        return -1
    else:
        mid = len(lst)//2
        if lst[mid] == key:
            return mid
        else:
            if key < lst[mid]:
                return binary_search_with_recursion(lst[:mid], key)
            else:
                return binary_search_with_recursion(lst[mid+1:], key)