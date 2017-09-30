a = [1,2,3]
del a[0]

#print(a)
#print(a[-1])

import numpy as np


#print(np.zeros((2,2)))

#print(np.random.randint(0,5,3))


# for i, j in enumerate(3) :
#     print(i + ' '+ j)

# import sys
# print(sys.stdout.encoding)
#
# f = open("test.txt", 'w')
# for i in range(1, 4):
#     data = "%d \n" % i
#     f.write(data)
# f.close()

import operator
from functools import reduce
l = [[1,2,3],[4,5,6,[66]], [7], [8,9]]
print(reduce(operator.concat, l))



