def count(a):
    l=0
    r=0
    for i in range(len(a)):
        if a[i]=='(':
            l+=1
        if a[i]==')':
            r+=1
        if l<r:
            return 1000
    else:
        if r!=l:
            return 1000
        else:
            return r
t=int(input())
for i in range(t):   
    a=input()

    if count(a)==1000:
        print('0')
    else:
        print(count(a))