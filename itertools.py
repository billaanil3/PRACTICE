import itertools
import operator
'''
data = [1, 2, 3, 4, 5]
#result = itertools.accumulate(data, operator.mul)
result = list(itertools.permutations([1,2,3], 2))
for each in result:
    print(each)       '''
'''
shapes = ['circle', 'triangle', 'square',]
result = itertools.combinations(shapes, 2)
for each in result:
    print(each)   '''
'''
shapes = ['circle', 'triangle', 'square',]
result = itertools.combinations_with_replacement(shapes, 2)
for each in result:
    print(each)  '''
'''
for i in itertools.count(10,3):
    print(i)
    if i > 20:
        break   '''

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
try:
   for color in itertools.cycle(colors):
      print(color)
      raise StopIteration


