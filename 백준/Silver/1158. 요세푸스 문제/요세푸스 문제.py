import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())
q = deque(range(1,N+1))
print('<',end='')
while len(q)!=1:
  q.rotate(-K+1)
  print(q.popleft(),end = ', ')
print(q[0],end='>')