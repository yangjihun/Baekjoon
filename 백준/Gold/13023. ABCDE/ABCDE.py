#13023
N,M = map(int,input().split())
arrive = False
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)

def DFS(n,depth):
  global arrive
  if depth==5:
    arrive = True
    return
  visited[n] = True
  for i in A[n]:
    if not visited[i]:
      DFS(i, depth+1)
  visited[n] = False

for _ in range(M):
  i,j = map(int,input().split())
  A[i].append(j)
  A[j].append(i)

for i in range(N):
  DFS(i,1)
  if arrive:
    break

if arrive:
  print(1)
else:
  print(0)