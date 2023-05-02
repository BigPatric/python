def che(a,o):
    s=0
    for i in str(a):
        s+=int(i)**o
    return s
b,N =input().split()
b=int(b)
k=len(N)
NN=int(N,b)
if che(N,k)==NN:
    print('YES')
else:
    print('NO')

   

