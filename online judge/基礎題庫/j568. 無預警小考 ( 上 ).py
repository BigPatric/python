"""

"""
def one(a):
    if a == 1:
        k=''    
    elif a==-1:
        k='-'
    else:
        k=str(a)
    return k+'x^2'
def two(b):
    if b>0:
        if b==1:
            return 'x'
        else:
            return '+'+str(b)+'x'
    elif b<0:
        if b==-1:
            return '-'+'x'
        else:
            return str(b)+'x'

    else:
        return ''
def thr(c):
    if c>0:
        return '+'+str(c)
    elif c<0:
        return str(c)
    else:
        return ''


t=int(input())
for i in range(t):
    n=int(input())
    print('請使用配方法解下列一元二次方程式')
    count=1
    for j in range(n):
        a,b,c=input().split()
        a=int(a)
        b=int(b)
        c=int(c)
        print(str(count)+'. '+one(a)+two(b)+thr(c)+'=0')




        count+=1
    print('考試要加油口屋')
