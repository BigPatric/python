import statistics
from statistics import mean
A=input().split()
A=list(map(int,A))
while True:
    try:  
        num = statistics.mode(A)
        P = A.count(num)
        break
    except:
        P=1
        break
A=list(set(A))
A.sort()
A=A[::-1]
print(P,*A)            