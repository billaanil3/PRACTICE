# class ABC():
#     i=10
#     def m1(self):
#         i=12
#         print i
#     # print i

class AB():
    i=10
    def m2(self):
        j=11
        i=30
        print i
        print j
    # print A.i
a = AB()
a.m2()
print a.i
