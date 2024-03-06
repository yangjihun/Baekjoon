N = int(input())
db = [[0]*10 for _ in range(N+1)]
for i in range(1,10):
  db[1][i] = 1

for i in range(2,N+1):
  for j in range(10):
    if j==0:
      db[i][j] = db[i-1][1]
    elif j==9:
      db[i][j] = db[i-1][8]
    else:
      db[i][j] = db[i-1][j-1]+db[i-1][j+1]
print(sum(db[N])%1000000000)