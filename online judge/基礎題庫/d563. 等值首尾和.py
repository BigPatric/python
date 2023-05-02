from sys import stdin
from itertools import accumulate

x=[int(x) for x in stdin.readline().split()]
a=x[1:]
b=a[::-1]
a=set(accumulate(a))
b=set(accumulate(b))


print(len(a&b))