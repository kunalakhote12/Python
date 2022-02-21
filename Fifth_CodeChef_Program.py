n=int(input())
co=0
ce=0
li=list(map(int,input().split(" ")))
for i in li:
    if i%2==0:
        ce+=1
    else:
        co+=1
if (co>=ce):
    print("NOT READY")
else:
    print("READY FOR BATTLE")
