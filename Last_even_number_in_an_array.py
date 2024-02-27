s=int(input())
li=list(map(int,input().split()))
lee=0
for i in li:
    if i%2==0:
        lee=i
print(lee)