size=int(input())
li=list(map(int,input().split()))
ev=0
od=0
for i in range(size):
    if i%2==0:
        ev=ev+li[i]
    else:
        od=od+li[i]
print(abs(ev-od))