N,M = map(int,input().split())
data = []
answer = 0
for _ in range(N):
  data.append(input())

for _ in range(M):
  i = input()
  if i in data:
    answer+=1
print(answer)