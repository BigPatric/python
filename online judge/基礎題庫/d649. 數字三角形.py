while True:
    n=int(input())
    if n==0:
        break
    else:
                  
          for j in range(n):
              print('_'*(n-j-1)+'+'*(j+1))
