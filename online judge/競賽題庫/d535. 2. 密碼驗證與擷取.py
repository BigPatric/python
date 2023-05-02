def Check(a):
    x=a[::-1]
    if x == a:
        return 1
    else:
        return 0

def SecCh(a):
    
    for j in range(1,len(a)):
        if int(a[j]) > int(a[j-1])*2:
            return 0
    else:
        return 1





while True:
    try:
        One = input()

        if Check(One)==1:
            if SecCh(One)==1:
                x=[]
                for j in One:
                    if int(j)%2==0:
                        x.append(j)
                if len(x)==0:
                    print('0')
                else:
                    for c in x:
                        print(c,end='')        



            else:
                print('INCORRECT')


        else:
            print('INCORRECT')



    except:
        break