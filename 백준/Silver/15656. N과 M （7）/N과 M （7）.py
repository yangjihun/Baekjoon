N,M = map(int,input().split())
num_list = sorted(list(map(int,input().split())))
li = []

def dfs():
    if len(li)==M:
        print(' '.join(map(str,li)))
        return
    for i in range(N):
        li.append(num_list[i])
        dfs()
        li.pop()
dfs()