# 1260
from collections import deque

N,M,V = map(int,input().split())
visited = [False] * (N+1)
A = [[] for _ in range(N+1)]

def DFS(n):
  print(n,end=' ')
  visited[n] = True
  for i in A[n]:
    if not visited[i]:
      visited[i] = True
      DFS(i)

def BFS(n):
  queue = deque()
  queue.append(n)
  visited[n] = True
  while queue:
    now_Node = queue.popleft()
    print(now_Node,end=' ')
    for i in A[now_Node]:
      if not visited[i]:
        visited[i] = True
        queue.append(i)

for _ in range(M):
  i,j = map(int,input().split())
  A[i].append(j)
  A[j].append(i)
  
for i in range(N+1):
  A[i].sort()

DFS(V)
print()
visited = [False] * (N+1)
BFS(V)