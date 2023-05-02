def Eng(j):
    j=str(j)
    s=0
    s+=int(j[1])*9
    s+=int(j[0])
    return s
n=input()
S=0
e=n[0]
if e=='A':
    S+=Eng(10)
if e=='B':
    S+=Eng(11)
if e=='C':
    S+=Eng(12)
if e=='D':
    S+=Eng(13)
if e=='E':
    S+=Eng(14)
if e=='F':
    S+=Eng(15)
if e=='G':
    S+=Eng(16)
if e=='H':
    S+=Eng(17)
if e=='I':
    S+=Eng(34)
if e=='J':
    S+=Eng(18)
if e=='K':
    S+=Eng(19)
if e=='L':
    S+=Eng(20)
if e=='M':
    S+=Eng(21)
if e=='N':
    S+=Eng(22)
if e=='O':
    S+=Eng(35)
if e=='P':
    S+=Eng(23)
if e=='Q':
    S+=Eng(24)
if e=='R':
    S+=Eng(25)
if e=='S':
    S+=Eng(26)
if e=='T':
    S+=Eng(27)
if e=='U':
    S+=Eng(28)
if e=='V':
    S+=Eng(29)
if e=='W':
    S+=Eng(32)
if e=='X':
    S+=Eng(30)
if e=='Y':
    S+=Eng(31)
if e=='Z':
    S+=Eng(33)

for i in range(1,9):
    S+=int(n[i])*(9-i)
S+=int(n[9])
if S%10==0:
    print('real')
else:
    print('fake')