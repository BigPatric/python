n=input()
s=input().split()
s=list(map(int,s))
s.sort() 
print(*s)
a=len(s)
v=[]
v.append(s[0])
for i in range(1,len(s)):   
    if s[i]!=s[i-1]:
        v.append(s[i])
v.reverse()
print(*v)
    