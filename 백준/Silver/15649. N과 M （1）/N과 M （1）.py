N,M = map(int,input().split())

li = []

def dfs():
    if len(li)==M:
        print(' '.join(map(str,li)))
    for i in range(1,N+1):
        if i not in li:
            li.append(i)
            dfs()
            li.pop()
dfs()