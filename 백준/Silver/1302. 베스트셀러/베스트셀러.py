import sys
input = sys.stdin.readline

N = int(input())
li = []
result = []

for _ in range(N):
  li.append(input())
m = set(li)
di = dict(zip(m,[0]*len(m)))
for k in li:
  di[k]+=1

m = max(di.values())
for i in di:
  if di[i]==m:
    result.append(i)
print(sorted(result)[0])