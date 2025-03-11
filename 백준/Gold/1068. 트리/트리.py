import sys
input = sys.stdin.readline

N = int(input())
node = list(map(int,input().split()))
kill = int(input())
answer = 0

def DFS(n,node):
    node[n] = -2
    for i in range(len(node)):
      if n==node[i]:
        DFS(i,node)

DFS(kill,node)

for i in range(N):
  if node[i]!=-2 and i not in node:
    answer+=1
print(answer)