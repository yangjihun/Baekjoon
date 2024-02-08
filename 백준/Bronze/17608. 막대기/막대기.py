import sys
input = sys.stdin.readline
N = int(input())
li = []
result = 0
for _ in range(N):
  li.append(int(input()))
li = li[::-1]
key = 0
for i in li:
  if i>key:
    result+=1
    key = i
print(result)