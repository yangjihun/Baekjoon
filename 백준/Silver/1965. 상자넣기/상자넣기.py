import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int,input().split()))
result = [1 for _ in range(n)]

for i in range(n):
  for j in range(i,n):
    if li[i]<li[j]:
      result[j] = max(result[i]+1,result[j])
print(max(result))