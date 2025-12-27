import sys
import heapq

input = sys.stdin.readline
pq = []

V,E = map(int,input().split())
start = int(input())
INF = 10**18

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    s,e,v = map(int,input().split())
    graph[s].append((e,v))

dist = [INF] * (V + 1)
dist[start] = 0
heapq.heappush(pq,(0,start))
while pq:
    value,num = heapq.heappop(pq)
    
    for next_n,next_v in graph[num]:
        next_v = next_v + value
        if next_v < dist[next_n]:
            dist[next_n] = next_v
            heapq.heappush(pq,(next_v,next_n))
for i in range(1,V+1):
    if dist[i]==INF:
        print("INF")
    else:
        print(dist[i])