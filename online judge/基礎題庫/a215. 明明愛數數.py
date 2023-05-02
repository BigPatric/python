while True:
    try:
        n,m=input().split()
        n=int(n)
        m=int(m)
        s=n
        count=1
        while s<=m:
            count+=1
            s+=n+1
            n+=1
            
        print(count)

    except:
        break