N,K = map(int,input().split())
li= []
answer = 0
for _ in range(N):
  li.append(int(input()))

li = li[::-1]

for i in li:
  answer+=K//i
  K = K%i
print(answer)