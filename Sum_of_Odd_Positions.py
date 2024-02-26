s=int(input())
li=list(map(int,input().split()))
odS=0
for i in range(s):
    if i%2!=0:
        odS+=li[i]
print(odS)