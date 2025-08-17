N,M = map(int,input().split())
num_list = sorted(list(map(int,input().split())))
li = []
visited = [False] * N

def dfs():
    check = 0
    if len(li)==M:
        print(' '.join(map(str,li)))
        return
    for i in range(N):
        if check!=num_list[i] and not visited[i]:
            visited[i] = True
            check = num_list[i]
            li.append(num_list[i])
            dfs()
            li.pop()
            visited[i] = False
dfs()