def check(u):
    u=str(u)
    l=len(u)
    s=0
    for k in u:
        s+=int(k)**l
    if s== int(u):
        return 1
    else:
        return 0


m,n=input().split()
m=int(m)
n=int(n)
j=0
for i in range(m,n+1):
    if check(i)==1:
        print(i,end=' ')
        j+=1
if j==0:
    print('none')