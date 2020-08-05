import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  # or / in Python 2

n = 1832

m = 871

a = []
for i in range(1,n+1):
    if i >= m:
        a.append(ncr(n,i))


print(sum(a)%1000000)

