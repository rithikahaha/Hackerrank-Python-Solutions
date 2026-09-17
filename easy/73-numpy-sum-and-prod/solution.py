import numpy

n, m = map(int, input().split())
arr = numpy.array([input().split() for _ in range(n)], int)

col_sum = numpy.sum(arr, axis=0)
print(numpy.prod(col_sum))
