# n = int(input("Enter a no.of rows:"))
# for i in range(n):
#     for j in range(i + 1):
#         print "*",
#     print
# Enter a no.of rows:5
# *
# * *
# * * *
# * * * *
# * * * * *
from __future__ import print_function
n = int(input("Enter a no.of rows:"))
for row in range(n):
    for col in range(n):
        if col == 0 or row == (n-1) or row == col:
            print ("*", end=" ")
        else:
            print(end=" ")
    print()

# Enter a no.of rows:5
# *
# * *
# *  *
# *   *
# * * * * *