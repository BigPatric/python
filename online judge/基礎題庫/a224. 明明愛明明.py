while True:
    try:
        s=input()
        s=''.join(e for e in s if e.isalnum())
        s.lower()
        x=s[::-1]

        if x==s:
            print('yes')
        else:
            print('no')
    except:
        break