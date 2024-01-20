import sys
from collections import deque

N = int(input())
deq = deque()
for _ in range(N):
  i = sys.stdin.readline().split()
  if i[0]=='1':
    deq.appendleft(i[1])
  elif i[0]=='2':
    deq.append(i[1])
  elif i[0]=='3':
    print(deq.popleft() if deq else -1)
  elif i[0]=='4':
    print(deq.pop() if deq else -1)
  elif i[0]=='5':
    print(len(deq))
  elif i[0]=='6':
    print(0 if deq else 1)
  elif i[0]=='7':
    print(deq[0] if deq else -1)
  elif i[0]=='8':
    print(deq[-1] if deq else -1)