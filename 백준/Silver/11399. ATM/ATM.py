N = int(input())
li = list(map(int,input().split()))
answer = 0
li.sort()

for i in range(N):
  answer+=li[i]*(N-i)
print(answer)