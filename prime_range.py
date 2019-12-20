# lower = int(input("Enter the lower range:"))
# upper = int(input("Enter the upper range:"))

# for num in range(lower, upper + 1):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 print "Not Prime"
#                 break
#         else:
#             print "Prime"

num = int(input("Enter the number:"))
if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print "Not Prime"
                break
        else:
            print "Prime"
