import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int,input().split()))
A = [0]*N
A[0] = li[0]
for i in range(1,N):
  for j in range(i):
    if li[i]>li[j]:
      A[i] = max(A[i],A[j]+li[i])
  if A[i]==0:
    A[i] = li[i]
print(max(A))