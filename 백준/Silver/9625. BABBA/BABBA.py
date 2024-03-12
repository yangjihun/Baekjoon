import sys
input = sys.stdin.readline
N = int(input())
li = []
li.append([0,1])
li.append([1,1])
for i in range(2,N):
  li.append([li[-1][0]+li[-2][0],li[-1][1]+li[-2][1]])
print(li[N-1][0],li[N-1][1])