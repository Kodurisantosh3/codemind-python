num=int(input())
m=int(input())
for val in range(num,m+1):
  santu=val
  s=0
  a=0
  while val:
    d=val%10
    val=val//10
    s+=1
    if d!=0:
       if santu%d==0:
           a+=1
  if s==a:
      print(santu,end=' ')