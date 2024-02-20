N  = int(input())
date = [0]*N
value = [0]*N
A = [0]*(N+1)
for i in range(1,N+1):
  date[N-i], value[N-i] = map(int,input().split())

for i in range(1,N+1):
  if date[i-1]==1:
    A[i] = A[i-1]+value[i-1]
  elif date[i-1]>i:
    A[i] = A[i-1]
  else:
    A[i] = max(A[i-date[i-1]]+value[i-1],A[i-1])
print(A[N])