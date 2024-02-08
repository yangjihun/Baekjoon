import sys
input = sys.stdin.readline
N = int(input())
li = []

for _ in range(N):
  num = int(input())
  if not li:
    li.append(num)
  elif li[-1]>num:
    li.append(num)
  else:
    while li[-1]<=num:
      li.pop()
      if not li:
        break
    li.append(num)
print(len(li))