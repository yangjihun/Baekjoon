import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int,input().split()))
A = [1]*N
for i in range(1,N):
  for j in range(i):
    if li[i]<li[j]:
      A[i] = max(A[j]+1,A[i])
print(max(A))