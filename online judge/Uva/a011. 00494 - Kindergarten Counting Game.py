while True:
    try:
        a=input()
        count=0
        one=0
        for i in a:
            if i == ' ':
                count+=1
        b=a.split()
        for i in b:
            if len(b[i])==1:
                one+=1
        print(count+1-one)

    except:
        break




