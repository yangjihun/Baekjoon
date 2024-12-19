from collections import deque

N = int(input())
q = deque(N-i for i in range(N))
li = []

while len(q)!=1:
  li.append(q.pop())
  q.rotate(1)

li.append(q[0])

print(' '.join(str(i) for i in li))