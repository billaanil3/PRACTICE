def most_courses(dict):
    count = 0
    name = ''

    for teacher, course in dict.items():
        # print teacher
        # print type(course)
        if type(course) is list and len(course) >= count:
            print "IF BLOCK"
            name = teacher
        elif count == 0:
            print "ELSE BOCK-------------", teacher
            name = teacher
            print "--------------------",teacher
    return name
# stats = {'a':1000, 'b':3000, 'c': 100}
stats = {'is': 2, 'a': 4, 'e': 3, 'good': 10}
print most_courses(stats)
