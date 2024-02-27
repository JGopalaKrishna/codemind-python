s=int(input())
li=list(map(int,input().split()))
lod=0
for i in li:
    if i%2!=0:
        lod=i
print(lod)