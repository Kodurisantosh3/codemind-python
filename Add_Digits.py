def add_digit(a):
    s=0
    while a>0:
        r=a%10
        s+=r
        a=a//10
    return s
n=int(input())
while n>9:
    n=add_digit(n)
print(n)