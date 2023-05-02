a,b=input().split()
a=a.replace(b,'')
c=a[::-1]
if a==c:
    print('Yes')
else:
    print('No')