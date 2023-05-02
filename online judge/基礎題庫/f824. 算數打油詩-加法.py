while True:
    try:

        Chi={
        '一':'1',
        '二':'2',
        '三':'3',
        '四':'4',
        '五':'5',
        '六':'6',
        '七':'7',
        '八':'8',
        '九':'9',
        '十':'10',
        '有':'+',
        '又':'+',
        '加':'+'
        }
        Num={
        1:'一',
        2:'二',
        3:'三',
        4:'四',
        5:'五',
        6:'六',
        7:'七',
        8:'八',
        9:'九',
        10:'十'
        }
        n=input()
        a=Chi[n[0]]
        c=Chi[n[2]]
        b=Chi.get(n[1],'0')
        if b=='0':
            print('謬')
        else:
            ans=int((eval(a+b+c)))
            if ans==20:
                print('二十')
            elif ans>10 and a<20:
                print('十'+Num[ans-10])
            else:
                print(Num[ans])

    except:
        break