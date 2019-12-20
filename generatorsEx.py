import memory_profiler as mem_profile
import random
import time

names = ['John','Corey','Adam','Steve','Rick','Thomas']
majors = ['Math','Engineering','CS','Arts','Business']

# print 'Memory (Before):{}Mb'.format(mem_profile.memory_usage_resource())
print('Memory (Before): ' + str(mem_profile.memory_usage()) + 'MB' )

#Normal function
def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id':i,
                    'name':random.choice(names),
                    'major':random.choice(majors)
                }
        result.append(person)
    return result

# Generator Function
def people_generator(num_people):
     for i in range(num_people):
        person = {
                    'id':i,
                    'name':random.choice(names),
                    'major':random.choice(majors)
                }
        yield person    

t1 = time.clock()
# people = people_list(10000000)
# print people
people = people_generator(10000000)
# print people
# for peo in people:
#     print peo
t2 = time.clock()

# print "Memory (After) : {}Mb".format(mem_profile.memory_usage_resource())
print('Memory (After) : ' + str(mem_profile.memory_usage()) + 'MB')
print "Took {} seconds".format(t2-t1)
print "*************************************"