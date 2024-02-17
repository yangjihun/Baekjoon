from collections import deque
import sys

input = sys.stdin.readline
n,m = map(int,input().split())
li = deque(range(1,n+1))
a = list(map(int,input().split()))
result = 0

for i in a:
  k = li.index(i)
  if k<=len(li)//2:
    result += k
    li.rotate(-k)
    li.popleft()
  else:
    result += len(li)-k
    li.rotate(-k)
    li.popleft()
print(result)