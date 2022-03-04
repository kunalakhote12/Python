# cook your dish here
s=input()
t=int(input())
for i in range(t):
    sc=input()
    re=True
    for x in sc:
        if x not in s:
            re=False
            break
        '''else:
            re=False
            break;'''
    if re:
        print("Yes")
    else:
        print("No")