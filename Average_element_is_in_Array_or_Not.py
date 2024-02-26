s=int(input())
li=list(map(int,input().split()))
avr=int(sum(li)/s)
if avr in li:
    print("True")
else:
    print("False")