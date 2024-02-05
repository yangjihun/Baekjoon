li = sorted(list(map(int,input().split())))

for i in range(1,li[0]*li[1]*li[2]+1):
  n = 0
  for k in li:
    if i%k==0:
      n+=1
  if n>=3:
    print(i)
    break