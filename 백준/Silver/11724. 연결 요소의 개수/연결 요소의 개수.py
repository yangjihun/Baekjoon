import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N,M = map(int,input().split())
li = [[] for _ in range(N+1)]
visited = [False]*(N+1)
count = 0
def BFS(v):
  visited[v] = True
  for i in li[v]:
    if not visited[i]:
      BFS(i)

for i in range(M):
  a,b = map(int,input().split())
  li[a].append(b)
  li[b].append(a)

for i in range(1,N+1):
  if not visited[i]:
    count+=1
    BFS(i)
print(count)