a=input().split()
n=int(a[0])
x=a[1:len(a)]
x=list(map(int,x))
x.sort()
if x[-1]-x[0]+1==n:
    print("{0} {1} yes".format(x[0],x[-1]))
else:
    print("{0} {1} no".format(x[0],x[-1]))