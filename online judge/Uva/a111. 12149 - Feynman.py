while True:
    N=int(input())
    if N==0:
        break
    else:
        ans=N*(N+1)*(2*N+1)
        ans/=6
        print(int(ans))

