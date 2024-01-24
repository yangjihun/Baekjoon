import sys
input = sys.stdin.readline

n = int(input())
d = dict()
ans = []
for _ in range(n):
  k = input().split()
  if k[1]=="enter":
    d[k[0]] = 1
  elif k[1]=="leave":
    d[k[0]] = 0

for i in d:
  if d[i]==1:
    ans.append(i)

for i in sorted(ans)[::-1]:
  print(i)