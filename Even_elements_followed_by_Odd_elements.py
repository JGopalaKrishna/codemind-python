size=int(input())
ar=list(map(int,input().split()))
eo=[]
for i in ar:
    if i%2==0:
        eo.append(i)
for i in ar:
    if i%2!=0:
        eo.append(i)
for i in eo:        
    print(i,end=" ")        