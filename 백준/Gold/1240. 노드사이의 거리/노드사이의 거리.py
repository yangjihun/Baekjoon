N,M = map(int,input().split())
li = [[] for _ in range(N+1)]
for i in range(N-1):
    a,b,dist = map(int,input().split())
    li[a].append([b,dist])
    li[b].append([a,dist])

def DFS(num1, num2, sum, visited):
    for i in li[num1]:
        if i[0]==num2:
            return (sum+i[1])
        if not visited[i[0]]:
            visited[i[0]] = True
            result = DFS(i[0], num2, sum+i[1], visited)
            if result is not None:
                return result
    

for _ in range(M):
    a,b = map(int,input().split())
    visited = [False] * (N+1)
    visited[a] = True
    print(DFS(a,b,0, visited))