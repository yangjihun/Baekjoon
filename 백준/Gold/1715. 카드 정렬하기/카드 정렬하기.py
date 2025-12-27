import sys
import heapq

N = int(input())
input = sys.stdin.readline
pq = []
result = 0

for _ in range(N):
    heapq.heappush(pq,int(input()))

while len(pq) >= 2:
    sum = heapq.heappop(pq) + heapq.heappop(pq)
    result += sum
    heapq.heappush(pq,sum)
print(result)