#2178
from collections import deque

N,M = map(int,input().split())
A = list([] for _ in range(N))
visited = [[False]*M for _ in range(N)]
for k in range(N):
  for v in input():
    A[k].append(int(v))

def BFS(a,b):
  queue = deque()
  queue.append([a,b])
  visited[a][b] = True
  while queue:
    i,j = queue.popleft()
    if i<N-1 and A[i+1][j]==1 and not visited[i+1][j]:
      A[i+1][j]+=A[i][j]
      visited[i+1][j] = True
      queue.append([i+1,j])
    if i>0 and A[i-1][j]==1 and not visited[i-1][j]:
      A[i-1][j]+=A[i][j]
      visited[i-1][j] = True
      queue.append([i-1,j])
    if j<M-1 and A[i][j+1]==1 and not visited[i][j+1]:
      A[i][j+1]+=A[i][j]
      visited[i][j+1] = True
      queue.append([i,j+1])
    if j>0 and A[i][j-1]==1 and not visited[i][j-1]:
      A[i][j-1]+=A[i][j]
      visited[i][j-1] = True
      queue.append([i,j-1])
BFS(0,0)
print(A[N-1][M-1])