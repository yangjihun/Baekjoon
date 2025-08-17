N,M = map(int,input().split())
li = []
num_list = sorted(list(map(int,input().split())))

def dfs(num):
    if len(li)==M:
        print(' '.join(map(str,li)))
        return
    for i in range(N):
        if num_list[i] not in li:
            li.append(num_list[i])
            dfs(i+1)
            li.pop()
dfs(1)