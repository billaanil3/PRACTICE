# # def m1():
# #     i = 1
# #     yield i
# #     i = i + 1
# #     yield i

# # # m1 = m1()
# # # print (m1.next())
# # # print (m1.next())
# # # Other way to call generator
# # for i in m1():
# #     print i


# # def fib(limit):
# #     a = 0
# #     b = 1
# #     while a < limit:
# #         yield a
# #         a = b
# #         b = a + b

# # # fib(5)
# # # limit = 5
# # for i in fib(5):
# #     print i

# # A simple generator for Fibonacci Numbers
# def fib(limit):

#     # Initialize first two Fibonacci Numbers
#     a = 0
#     b = 1

#     # One by one yield next Fibonacci Number
#     while a < limit:
#         yield a
#         a, b = b, a + b

# # # Create a generator object
# x = fib(5)

# # # Iterating over the generator object using next
# print(x.next()); # In Python 3, __next__()
# print(x.next());
# print(x.next());
# print(x.next());
# print(x.next());
# # print(x.next()); StopIteration error will come

# # Iterating over the generator object using for
# # in loop.
# # print("\nUsing for in loop")
# # for i in fib(5):
# #     print(i)


# class A():

#     def __init__(self):
#         self.name = "Anil"

#     def set_name(self, n):
#         name = n
#         print name

#     def get_name(self):
#         print self.name

# a = A()
# a.set_name("Vijay")
# a.get_name()


# s1 = 'ABCD'
# s2 = 'PQR'
# s3 = ''
# for i in range(len(s1) + 1):
#     if i! = 0:
#         for j in range(i):
#             s3 = s1[:i] + s2[j:]
#         print s3

# num = sum of digits power of length

for i in range(1000):
    num = i
    result = 0
    n = len(str(i))
    while i!=0:
        rem = i % 10
        result = result + rem ** n
        i = i // 10
    if num == result:
        print "--------", num
