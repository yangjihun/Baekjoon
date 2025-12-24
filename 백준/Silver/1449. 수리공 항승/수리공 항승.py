N,L = map(int,input().split())
li = list(map(int,input().split()))
visited = [False for _ in range(1001)]
li.sort()
answer = 0

for poor in li:
    if not visited[poor]:
        visited[poor:poor+L] = [True for _ in range(L)]
        answer+=1
print(answer)