N,M = map(int,input().split())
num_list = sorted(list(map(int,input().split())))
li = []
def dfs(num):
    check = 0
    if len(li)==M:
        print(' '.join(map(str,li)))
        return
    for i in range(N):
        if check!=num_list[i]:
            check = num_list[i]
            li.append(num_list[i])
            dfs(i)
            li.pop()
dfs(0)