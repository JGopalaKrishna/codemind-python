def prime(n):
    if(n==1):return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

num=int(input())
s="Not Mega Prime"
if(prime(num)):
    while(num>0):
        re=num%10
        if(prime(int(re))):
            num/=10
            s="Mega Prime"
        else:
            s="Not Mega Prime"
            break
print(s)    