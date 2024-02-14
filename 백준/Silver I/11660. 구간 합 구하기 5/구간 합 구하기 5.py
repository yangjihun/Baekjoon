import sys
input = sys.stdin.readline

N,M = map(int,input().split())
li = [[0]*N for _ in range(N)]
A = [[0]*(N+1) for _ in range(N+1)]

for i in range(N):
  li[i] = list(map(int,input().split()))

for i in range(1,N+1):
  for j in range(1,N+1):
    A[i][j] = li[i-1][j-1]+A[i-1][j]+A[i][j-1]-A[i-1][j-1]

for _ in range(M):
  x1,y1,x2,y2 = map(int,input().split())
  print(A[x2][y2]-A[x2][y1-1]-A[x1-1][y2]+A[x1-1][y1-1])