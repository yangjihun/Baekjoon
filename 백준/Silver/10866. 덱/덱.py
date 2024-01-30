from collections import deque
import sys
input = sys.stdin.readline
d = deque()

for _ in range(int(input())):
  n = input().split()
  if n[0]=="push_back":
    d.append(n[1])
  elif n[0]=="push_front":
    d.appendleft(n[1])
  elif n[0]=="pop_front":
    print(d.popleft() if d else -1)
  elif n[0]=="pop_back":
    print(d.pop() if d else -1)
  elif n[0]=="size":
    print(len(d))
  elif n[0]=="empty":
    print(0 if d else 1)
  elif n[0]=="front":
    print(d[0] if d else -1)
  elif n[0]=="back":
    print(d[-1] if d else -1)