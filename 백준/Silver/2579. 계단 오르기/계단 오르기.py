N = int(input())
li = []
d = [0]*N
for i in range(N):
  li.append(int(input()))
d[0] = li[0]
if N<2:
  print(li[0])
elif N<=2:
  print(li[0]+li[1])
else:
  d[1] = li[0]+li[1]
  for i in range(2,N):
    d[i] = max(d[i-3]+li[i-1],d[i-2])+li[i]
  print(d[-1])