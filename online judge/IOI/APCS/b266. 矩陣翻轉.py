def flip(A):### operation 1 A==array
    return A[::-1]

def spin(A):### operation 0 A==array turn 逆時
    X,Y,new=len(A[0]),len(A),[]##x=3y=4 X=4 Y=3

    for x in range(X-1,-1,-1):
        f=[]
        for y in range(Y):            
            f.append(A[y][x])###f=[1,2,3,4],[5,6,7,8],[9,10,11,12]
        new.append(f)###all=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        
        
    return new

r,c,m=input().split()
r=int(r)
c=int(c)
m=int(m)
B=[]
for i in range(r):
   t=input().split()
   B.append(t)
M=input().split()
M.reverse()

A=B
for i in M:
    if i=='1':
        A=flip(A)
    else:
        A=spin(A)

r=len(A)
c=len(A[0])
print(r,c)
for i in A:
    print(*i)

        