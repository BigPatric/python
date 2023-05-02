def check(n):
    s=0
    for j in range(3,n**0.5,2):
        if n%j==0:
            return 1
            break
    return 0

a,b=input().split()
a=int(a)
b=int(b)
ans=[]
for i in range(a,b+1):
    if i ==2 :
        ans[].append(2)
    elif i==3:
        ans[].append(3)
    elif i%2==0:
        continue
    else:
        if check(i)==0:
            ans[].append(i)
    print(len(ans))