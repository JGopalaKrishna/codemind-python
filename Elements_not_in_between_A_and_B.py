size=int(input())
ary=list(map(int,input().split()))
x,y=map(int,input().split())
suc=0
for i in range(size):
    if ary[i]>=x and ary[i]<=y:
        continue
    else:
        print(ary[i],end=" ")
        suc=1
if suc==0:
    print(-1)