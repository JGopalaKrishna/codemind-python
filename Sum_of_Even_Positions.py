s=int(input())
li=list(map(int,input().split()))
evS=0
for i in range(s):
    if i%2==0:
        evS+=li[i]
print(evS)