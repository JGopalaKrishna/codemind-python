size=int(input())
ary=list(map(int,input().split()))
count=0
for i in range(1,size-1):
    if(ary[i-1]%2!=0 and ary[i+1]%2!=0):
        if(ary[i]%2!=0):
            count+=1
print(count)            