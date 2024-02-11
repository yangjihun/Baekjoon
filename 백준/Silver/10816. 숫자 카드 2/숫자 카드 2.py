import sys
input = sys.stdin.readline

N = int(input())
Ndi = list(map(int,input().split()))
M = int(input())
Mdi = list(map(int,input().split()))
k = Ndi+Mdi
di = dict(zip(k,[0]*len(k)))
for i in Ndi:
  di[i]+=1
for i in Mdi:
  print(di[i],end=' ')