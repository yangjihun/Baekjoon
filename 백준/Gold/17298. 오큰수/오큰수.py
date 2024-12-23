N = int(input())
A = list(map(int,input().split()))
li = [0]
answer = [0 for _ in range(N)]
for i in range(1,N):
  while li and A[i]>A[li[-1]]:
    answer[li[-1]] = A[i]
    li.pop()
  li.append(i)

for i in range(N):
  if answer[i]==0:
    answer[i] = -1
print(' '.join(map(str,answer)))