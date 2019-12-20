from __future__ import print_function


def merge_sort(arr):
    if len(arr) >1 :

        mid = len(arr) // 2
        first_half = arr[:mid]
        second_half = arr[mid:]

        merge_sort(first_half)
        merge_sort(second_half)

        i = j = k = 0
        while i < len(first_half) and j < len(second_half):
            if first_half[i] < second_half[j]:
                arr[k] = first_half[i]
                i += 1
            else:
                arr[k] = second_half[j]
                j += 1
            k += 1

        while i < len(first_half):
            arr[k] = first_half[i]
            i += 1
            k += 1

        while j < len(second_half):
            arr[k] = second_half[j]
            j += 1
            k += 1


def printList(arr):
    for i in range(len(arr)):
        print (arr[i], end=" ")
    print ()

arr = [12, 11, 13, 5, 6, 7]
print ("Given array is", end="\n")
printList(arr)
merge_sort(arr)
print("Sorted array is: ", end="\n")
printList(arr)
