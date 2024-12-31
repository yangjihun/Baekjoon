# 1715
from queue import PriorityQueue
N = int(input())
pq = PriorityQueue()

for _ in range(N):
  pq.put(int(input()))

sum = 0

while pq.qsize()>1:
  data1 = pq.get()
  data2 = pq.get()
  temp = data1 + data2
  sum+=temp
  pq.put(temp)

print(sum)