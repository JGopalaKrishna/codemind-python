size=int(input())
ae=list(map(int,input().split()))
oe=[]
for i in ae:
    if i%2!=0:
        oe.append(i)
for i in ae:
    if i%2==0:
        oe.append(i)
for i in oe:
    print(i,end=" ")