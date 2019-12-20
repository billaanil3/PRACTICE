from __future__ import print_function

num = int(input("Enter the number of rows:"))
for i in range(0, num):
    for j in range(num - i):
        print (" ", end=" ")
    for j in range(1, i):
        print (j, end=" ")
    for i in range(i, 0, -1):
        print(i, end= " ")
    print()