size=int(input())
ary=list(map(int,input().split()))
x,y=map(int,input().split())
su=0
stop=0
for i in range(size):
    if ary[i]>=x and ary[i]<=y:
        continue
    else:
        su+=ary[i]
print(su)