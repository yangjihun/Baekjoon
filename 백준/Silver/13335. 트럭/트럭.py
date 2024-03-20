import sys
from collections import deque
input = sys.stdin.readline

n,w,L = map(int,input().split())
truck = deque(map(int,input().split()))
bridge = deque(0 for _ in range(w))
weight = 0
result = 0

while truck or bridge:
  result+=1
  weight-=bridge.popleft()
  if truck:
    if weight+truck[0]>L:
      bridge.append(0)
    else:
      weight+=truck[0]
      bridge.append(truck.popleft())
print(result)