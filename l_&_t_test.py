# # ---------- Bubble Sort---------------
# lst = [14, 33, 27, 35, 10]
# for i in range(len(lst) - 1):
#     min_index = i
#     for j in range(i + 1, len(lst)):
#         if lst[min_index] > lst[j]:
#             min_index = j
#     lst[i], lst[min_index] = lst[min_index], lst[i]
# print "Sorted list:", lst
# ---------------------------------------------
# from __future__ import print_function

# num = int(input("Enter the number of rows:"))
# for i in range(0, num):
#     for j in range(num - i):
#         print (" ", end=" ")
#     for j in range(1, i):
#         print ('*', end=" ")
#     for i in range(i, 0, -1):
#         print('*', end=" ")
#     print()
# ----------------------------------------------
# import math, random, string
# # digits = "0123456789"
# digits = string.digits
# OTP=""
# for i in range(4):
#     OTP += digits[random.randint(1, 10)]
# print OTP
# --------------------------------------------------
# num = int(input("Enter a number:"))

# if num > 1:
#     for i in range(2, num // 2):
#         if (num % i) == 0:
#             print "Not Prime"
#             break
#     else:
#         print "prime"

# for num in range(10, 100):
#     for i in range(2, num // 2):
#         if (num % i) == 0:
#             # print "Not Prime"
#             break
#     else:
#         print "prime", num

# ------------------------------------------------------------------
# num = int(input("Enter a number:"))

# res = 0
# temp = num
# while num > 0:
#     rem = num % 10
#     res = res * 10 + rem
#     num = num // 10
# if temp == res:
#     print "Polindrome"
# else:
#     print "Not a Polindrome"

# -------------------------------------------------------------------
# from __future__ import print_function


# def merge_sort(arr):
#     if len(arr) > 1:

#         mid = len(arr) // 2
#         first_half = arr[:mid]
#         second_half = arr[mid:]

#         merge_sort(first_half)
#         merge_sort(second_half)

#         i = j = k = 0
#         while i < len(first_half) and j < len(second_half):
#             if first_half[i] < second_half[j]:
#                 arr[k] = first_half[i]
#                 i += 1
#             else:
#                 arr[k] = second_half[j]
#                 j += 1
#             k += 1

#         while i < len(first_half):
#             arr[k] = first_half[i]
#             i += 1
#             k += 1

#         while j < len(second_half):
#             arr[k] = second_half[j]
#             j += 1
#             k += 1


# def printList(arr):
#     for i in range(len(arr)):
#         print (arr[i], end=" ")
#     print ()

# arr = [12, 11, 13, 5, 6, 7]
# print ("Given array is", end="\n")
# printList(arr)
# merge_sort(arr)
# print("Sorted array is: ", end="\n")
# printList(arr)


# ---------------------------------------------------------------
from __future__ import print_function

num = int(input("Enter a number:"))
for i in range(0, num):
    for j in range(num - i):
        print (" ", end=" ")
    for j in range(1, i):
        print (j, end=" ")
    for i in range(i, 0, -1):
        print (i, end=" ")
    print ()
# for i in range(0, num):
#     for j in range(num - i):
#         print (" ", end=" ")
#     for j in range(1, i):
#         print ('*', end=" ")
#     for i in range(i, 0, -1):
#         print('*', end=" ")
#     print()
