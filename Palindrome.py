num=int(input())
rev=0
t=num
while num>0:
    r=num%10
    rev=rev*10+r
    num=num//10

if t==rev:
    print('True')
else:
    print('False')
