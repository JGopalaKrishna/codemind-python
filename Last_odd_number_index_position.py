s=int(input())
li=list(map(int,input().split()))
elePo=0
for i in range(s):
    if li[i]%2!=0:
        elePo=i
print(elePo)