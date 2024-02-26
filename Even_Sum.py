s=int(input())
li=list(map(int,input().split()))
evS=0
for i in li:
    if i%2==0:
        evS+=i
print(evS)