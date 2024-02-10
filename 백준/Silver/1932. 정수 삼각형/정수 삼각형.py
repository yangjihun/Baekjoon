n = int(input())
li = []
for _ in range(n):
  li.append(list(map(int,input().split())))

li = li[::-1]
for i in range(len(li)-1):
  for k in range(len(li[i])-1):
    li[i+1][k] += max(li[i][k],li[i][k+1])

print(li[-1][0])