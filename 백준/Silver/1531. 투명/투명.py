import sys
input = sys.stdin.readline
N,M = map(int,input().split())
pic = [[0]*100 for _ in range(100)]
result = 0

for _ in range(N):
  x1,y1,x2,y2 = map(int,input().split()) 
  for x in range(x1-1,x2):
    for y in range(y1-1,y2):
      pic[x][y]+=1

for i in pic:
  for j in i:
    if j>M:
      result+=1
print(result)