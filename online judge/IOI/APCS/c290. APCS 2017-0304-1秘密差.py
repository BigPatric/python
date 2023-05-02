x=input()
A=0
B=0
for i in range(0,len(x)):
    if i%2==0:
        A+=int(x[i])
    else:
        B+=int(x[i])
ans=A-B
if ans<0:
    ans*=(-1)

print(ans)