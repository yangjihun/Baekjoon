N = int(input())
visited = [[False for _ in range(N)] for _ in range(N)]
li = [[] for _ in range(N)]
answer = 0
hometown = []
total = 0

for i in range(N):
    li[i] = list(map(int,list(input())))

nx = [0,1,0,-1]
ny = [1,0,-1,0]

def dfs(x,y):
    global li, visited, total
    total+=1
    visited[y][x] = True
    for i in range(4):
        next_x = x + nx[i]
        next_y = y + ny[i]
        if 0<=next_y<N and 0<=next_x<N and li[next_y][next_x]!=0 and not visited[next_y][next_x]:
            dfs(next_x,next_y)

for i in range(N):
    for j in range(N):
        if li[i][j]!=0 and not visited[i][j]:
            total = 0
            dfs(j,i)
            answer+=1
            hometown.append(total)

print(answer)
[print(x) for x in sorted(hometown)]