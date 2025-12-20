from collections import deque

M,N = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(N)]
queue = deque()
key = 0
result = 0

for i in range(N):
    for j in range(M):
        if li[i][j]==1:
            queue.append((i,j))

nx = [1,0,-1,0]
ny = [0,1,0,-1]

while queue:
    i,j = queue.popleft()
    for next in range(4):
        ni = i + nx[next]
        nj = j + ny[next]
        if 0 <= ni < N and 0 <= nj < M and li[ni][nj]==0:
            li[ni][nj] = li[i][j] + 1
            queue.append((ni,nj))

for i in range(N):
    for j in range(M):
        result = max(result,li[i][j])
        if li[i][j]==0:
            key = 1

if key==0:
    print(result - 1 if result > 0 else 0)
else:
    print(-1)