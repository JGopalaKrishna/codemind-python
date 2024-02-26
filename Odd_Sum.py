s=int(input())
li=list(map(int,input().split()))
odS=0
for i in li:
    if i%2!=0:
        odS+=i
print(odS)