#bubble sort - O(n**2) - exchange
def bubble_sort(lst):
    for cnt in range(len(lst)-1, 0, -1):
        for i in range(cnt):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]

import random
lst = [random.randrange(100) for i in range(10)]
print(lst)
# bubble_sort(lst)

#insertion sort - O(n**2) - shift
def insertion_sort(lst):
    for i in range(1, len(lst)):
        current = lst[i]
        pos = i
        while pos>0 and lst[pos-1]>current:
            lst[pos] = lst[pos-1]   #shift
            pos -= 1
        lst[pos] = current

#merge sort - O(n * log n)
def merge_sort(lst):
    # print('Divide:', lst)
    if len(lst) > 1:
        mid = len(lst)//2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)
        i, j, k = 0, 0, 0

        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
    # print('Merge:', lst)

merge_sort(lst)
print(lst)
