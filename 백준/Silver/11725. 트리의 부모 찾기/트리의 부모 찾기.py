import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())

tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    s,e = map(int,input().split())
    tree[s].append(e)
    tree[e].append(s)

visited = [0] * (N+1)

def dfs(n):
    for i in tree[n]:
        if not visited[i]:
            visited[i] = n
            dfs(i)
dfs(1)
for i in range(2,N+1):
    print(visited[i])