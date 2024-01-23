M = int(input())
N = int(input())
first = 0
answer = 0
for i in range(M,N+1):
  key = 0
  for k in range(2,i+1):
    if k==i:
      answer+=i
      if first==0:
        first = i
    if i%k==0:
      key = 1
      break

if answer==0:
  print(-1)
else:
  print(answer)
  print(first)