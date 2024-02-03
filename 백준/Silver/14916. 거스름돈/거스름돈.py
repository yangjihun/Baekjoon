n = int(input())
count = 0
if n==1 or n==3:
  print(-1)
else:
  while n!=0:
    if n-5>=0:
      n-=5
      count+=1
    elif n%2==1:
      n+=5
      count-=1
      count+=n//2
      break
    else:
      count+=n//2
      break
  print(count)