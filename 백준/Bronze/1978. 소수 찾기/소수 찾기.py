N = int(input())
li = list(map(int,input().split()))
ans = 0
for i in li:
  if i==2:
    ans+=1
  for k in range(2,i):
    if i%k==0:
      break
    if k==(i-1):
      ans+=1
print(ans)