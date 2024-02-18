N = int(input())
li = [0,1]
if N==1:
  print(li[N])
else:
  for i in range(1,N+1):
    li.append(li[-2]+li[-1])
  print(li[-1]%10007)