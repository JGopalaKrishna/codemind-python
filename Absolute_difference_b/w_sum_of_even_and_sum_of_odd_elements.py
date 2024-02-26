s=int(input())
li=list(map(int,input().split()))
ev=0
od=0
for i in li:
    if i%2==0:
        ev+=i
    else:
        od+=i
print(abs(ev-od))