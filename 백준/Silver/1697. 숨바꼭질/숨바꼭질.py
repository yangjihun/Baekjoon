from collections import deque

N,K = map(int,input().split())
visited = [-1] * 100001

que = deque([N])
visited[N] = 0
while(que):
    num = que.popleft()
    if num==K:
        print(visited[K])
        break
    for i in [num-1,num+1,num*2]:
        if 0<=i<=100000 and visited[i]==-1:
            visited[i] = visited[num] + 1
            que.append(i)