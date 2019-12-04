import numpy as np
import P3 as p3
import math
import matplotlib.pyplot as plt
q = list(np.loadtxt("words.txt",dtype=str))

#wordsh = p3.PriorityQueue(math.inf)
#wordsh.elements = q


numlist = (10, 20, 50, 100, 200, 500)

naive = p3.timeit(numlist, p3.NaivePriorityQueue, 5)
heap = p3.timeit(numlist, p3.HeapPriorityQueue, 5)
python = p3.timeit(numlist, p3.PythonHeapPriorityQueue, 5)
'''
print(naive)
print(heap)
print(python)
'''
pl1 = plt.plot(numlist, naive, label = 'naive')
pl2 = plt.plot(numlist, heap, label = 'heap')
pl3 = plt.plot(numlist, python, label = 'python')

plt.title('Competition of running time')
plt.xlim(0, 500)
plt.xlabel('Number of Lists Merged')
plt.ylabel('Elapsed time in seconds')
plt.legend()
plt.show()
