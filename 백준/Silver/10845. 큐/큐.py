from collections import deque
import sys
input = sys.stdin.readline

que = deque()
for _ in range(int(input())):
  a = input().split()
  if a[0]=="push":
    que.append(a[1])
  elif a[0]=="pop":
    print(que.popleft() if que else -1)
  elif a[0]=="size":
    print(len(que))
  elif a[0]=="empty":
    print(0 if que else 1)
  elif a[0]=="front":
    print(que[0] if que else -1)
  elif a[0]=="back":
    print(que[-1] if que else -1)