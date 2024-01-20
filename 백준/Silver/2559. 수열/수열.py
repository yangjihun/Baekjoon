N,K = map(int,input().split())
temper = list(map(int,input().split()))
A = [0]*(N+1)
result = -100000000

for i in range(N):
  A[i+1] = A[i]+temper[i]

for i in range(N-K+1):
  mean = A[K+i]-A[i]
  if result<mean:
    result = mean
print(result)