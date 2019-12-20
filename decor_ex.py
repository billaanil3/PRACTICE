def test(func):
    def inner(a, b):
        if b < 0:
            print "WARN: Division wont happen"

        else:
            print "INFO: The result is : "
        return func(a, b)
    return inner


@test
def div(a, b):
    return a / b

print div(10, 2)
