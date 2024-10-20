n,d = map(int,input().split())
total = 0
li = []
for _ in range(n):
  li.append(int(input()))
  total += li[-1]
d = d/total
for i in li:
  print(int(i*d))