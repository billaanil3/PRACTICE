num = int(input("Enter a number:"))

if num > 1:
    for i in range(2, num//2):
        if (num % i) == 0:
            print "Not Prime"
            break
    else:
        print "prime"