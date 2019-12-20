class MyClass():
    a = 10

    def __init__(self):
        print "init"

    def func(self):
        print "Hello"

mc1 = MyClass()  # init
mc2 = MyClass()  # init
print mc1.a     # 10
print mc2.a     # 10
mc1.func()
print MyClass.a     # 10
print MyClass.func
print MyClass.__doc__
