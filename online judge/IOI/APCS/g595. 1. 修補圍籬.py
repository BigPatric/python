n=input()
h=input().split()
h=list(map(int,h))
all=0
if h[0]==0:
    h[0]=h[1]
    all+=h[1]
if h[-1]==0:
    h[-1]=h[-2]
    all+=h[-2]
for i in range(1,len(h)-1):
    if h[i]==0:
        a=h[i-1]
        b=h[i+1]
        h[i]=min(a,b)
        all+=min(a,b)
print(all)