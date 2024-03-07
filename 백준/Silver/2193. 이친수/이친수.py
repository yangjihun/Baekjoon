N = int(input())
if N==1:
  print(1)
else:
  dp = [[0,0] for _ in range(N+1)]
  dp[1] = [0,1]

  for i in range(2,N+1):
    dp[i][0], dp[i][1] = sum(dp[i-1]), dp[i-1][0]

  print(sum(dp[N]))