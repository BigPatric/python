while True :
    try:
        n = int(input())
        a=input().split()
        a=list(map(int,a))
        a.sort()
        print(a)
        '''for i in a:
            print(i,end=' ')
            '''


    except:
        break