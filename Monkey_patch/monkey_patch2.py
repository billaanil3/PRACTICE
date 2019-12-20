import monkey_patch1


def monkey_f(self):
    print "monkey-f()"

monkey_patch1.myClass.f = monkey_f
obj = monkey_patch1.myClass()
obj.f()
