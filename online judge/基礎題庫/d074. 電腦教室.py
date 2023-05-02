
while True:
    try: 
        n=int(input())
        for i in range(n):
            b=input().split()
            b=list(map(int,b))
            print(max(b))
    except:
        break