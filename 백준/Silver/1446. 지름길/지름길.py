import sys
input = sys.stdin.readline

N,D = map(int,input().split())
load = [0] * (D + 1)
fast = []

for _ in range(N):
  fast.append(list(map(int,input().split())))

for i in range(1, D + 1):
  n = D
  for s,e,l in fast:
    if e==i:
      n = min(n, load[s] + l)
  load[i] = min(load[i-1]+1, n)
print(load[D])