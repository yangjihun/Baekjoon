C = int(input())
N = int(input())

A = [[] for _ in range(C+1)]
li = [1]
visited = [False for _ in range(C+1)]
visited[1] = True
count = 0

for _ in range(N):
  a,b = map(int,input().split())
  A[a].append(b)
  A[b].append(a)

while li:
  num = li.pop()
  for i in A[num]:
    if not visited[i]:
      li.append(i)
      visited[i] = True
      count+=1

print(count)