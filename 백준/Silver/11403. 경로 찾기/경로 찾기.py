import sys
from collections import deque
input = sys.stdin.readline
queue = deque()
N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]

graph = [[] for _ in range(N)]
for i in range(N):
  for j in range(N):
    if matrix[i][j]==1:
      graph[i].append(j)



for num in range(N):
  visited = [False for _ in range(N)]
  answer = [0 for _ in range(N)]
  queue.append(num)
  while queue:
    for i in graph[queue.popleft()]:
      if not visited[i]:
        answer[i] = 1
        visited[i] = True
        queue.append(i)
  for i in answer:
    print(i,end=' ')
  print()