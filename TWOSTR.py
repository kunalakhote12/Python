# cook your dish here
t=int(input())
for i in range(t):
    s1=input()
    s2=input()
    res=True
    for x in range(len(s1)):
        if s1[x]=='?' or s2[x]=='?':
            res=True
        elif s1[x]!=s2[x]:
            res=False
            break
    if res:
        print("Yes")
    else:
        print("No")