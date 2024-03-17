size=int(input())
arry=list(map(int,input().split()))
count=0
for i in range(1,size-1):
    if(arry[i-1]%2==0 and arry[i+1]%2!=0 or arry[i-1]%2!=0 and arry[i+1]%2==0):
        count+=1
print(count)