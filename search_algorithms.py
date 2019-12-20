def linearSearch(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
            # print "element found at",i
    return -1
arr = [10,20,80,30,60,50,70,110,100,130,170]
x = 110
result = linearSearch(arr,x)
if result != -1:
    print "Element is present at index %d" % result
else:
    print "Element is not present in array"



'''def binarySearch(arr,left,right,x):
    if right >= left:
        mid = left+(right-left)/2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr,left,mid-1,x)
        else:
            return binarySearch(arr,mid+1,right,x)
    else:
        return -1
arr =  [2,3,4,10,40]
x = 10
result = binarySearch(arr,0,len(arr)-1,x)
# print result
if result != -1:
    print "Element is present at index %d" % result
else:
    print "Element is not present in array"

'''