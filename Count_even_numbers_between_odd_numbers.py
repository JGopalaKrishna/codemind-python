size=int(input())
ary=list(map(int,input().split()))
cou=0
for i in range(1,size-1):
    if ary[i-1]%2!=0 and ary[i+1]%2!=0:
        if ary[i]%2==0:
            cou+=1
print(cou)            