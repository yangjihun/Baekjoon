import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

M,N = map(int,input().split())
dp = [[] for _ in range(M)]
memo = [[-1] * N for _ in range(M)]
answer = 0

for i in range(M):
    dp[i] = list(map(int,input().split()))

arrow_x = [1,-1,0,0]
arrow_y = [0,0,1,-1]

def dfs(x,y):
    if x==N-1 and y==M-1:
        return 1
    
    if memo[y][x]!=-1:
        return memo[y][x]
    
    memo[y][x] = 0
    
    for i in range(4):
        next_x = x + arrow_x[i]
        next_y = y + arrow_y[i]
        if 0<=next_x<N and 0<=next_y<M and dp[next_y][next_x] < dp[y][x]:
            memo[y][x] += dfs(next_x,next_y)
    
    return memo[y][x]

print(dfs(0,0))
