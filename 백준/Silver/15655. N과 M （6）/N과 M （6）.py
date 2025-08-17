N,M = map(int,input().split())
num_list = sorted(list(map(int,input().split())))
li = []

def dfs(num):
    if len(li)==M:
        print(' '.join(map(str,li)))
        return
    for i in range(num,N):
        li.append(num_list[i])
        dfs(i+1)
        li.pop()
dfs(0)