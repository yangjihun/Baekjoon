import sys
input = sys.stdin.readline

N,M = map(int,input().split())
maps = [[] for _ in range(N+1)]
maps[0] = [0 for _ in range(M+1)]
for i in range(1,N+1):
  maps[i] = [0]+list(map(int,input().split()))

for i in range(1,N+1):
  for j in range(1,M+1):
    maps[i][j] += max(maps[i-1][j],maps[i][j-1],maps[i-1][j-1])
print(maps[-1][-1])