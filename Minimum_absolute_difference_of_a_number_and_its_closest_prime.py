def fun(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    print(abs(n-num))
    return True
num=int(input())
ne=num-1
po=num+1
if(not fun(num)):
    while(True):
        if(fun(ne) or fun(po)):
            break
        ne-=1
        po+=1