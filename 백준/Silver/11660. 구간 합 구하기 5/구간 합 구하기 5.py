import sys
input = sys.stdin.readline

N,M = map(int,input().split())
table = [[0 for _ in range(N+1)]]
A = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(N):
  l = [0] + list(map(int,input().split()))
  table.append(l)

for i in range(N):
  for j in range(N):
    A[i+1][j+1] = table[i+1][j+1] + A[i][j+1] + A[i+1][j] - A[i][j]

for _ in range(M):
  sx,sy,ex,ey = map(int,input().split())
  print(A[ex][ey]-A[sx-1][ey]-A[ex][sy-1]+A[sx-1][sy-1])