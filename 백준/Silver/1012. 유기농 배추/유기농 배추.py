import sys
sys.setrecursionlimit(10000)

T = int(input())
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def DFS(x,y):
  table[y][x] = 0
  for i in range(4):
    if 0<=x+dx[i]<=M-1 and 0<=y+dy[i]<=N-1 and table[y+dy[i]][x+dx[i]]==1:
      DFS(x+dx[i],y+dy[i])

for _ in range(T):
  M,N,K = map(int,input().split())
  table = [[0] * M for _ in range(N)]
  count = 0

  for i in range(K):
    x,y = map(int,input().split())
    table[y][x] = 1
    
  for i in range(N):
    for j in range(M):
      if table[i][j]==1:
        count+=1
        DFS(j,i)

  print(count)