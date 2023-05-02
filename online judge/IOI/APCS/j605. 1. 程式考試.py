K=int(input())
t=[]
s=[]
count = 0### severe error
for i in range(K):
    a,b=input().split()
    t.append(int(a))
    s.append(int(b))
    if int(b)==-1:
        count+=1
M=max(s)
SS=M-K-count*2
if SS<0:
    SS=0
for i in range(K):
    if s[i]==M:
        T=t[i]
        break

print(SS,T)