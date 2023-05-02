t=int(input())
for i in range(t):
    A=[]
    B=[]
    for j in range(10):
        a,b=input().split()
        
        A.append(a)
        A.append(b)
        b=int(b)
        B.append(b)
    k=max(B)
    print('Case #{0}:'.format(i+1))
    for j in range(20):
        if A[j]==str(k):
            print(A[j-1])
    