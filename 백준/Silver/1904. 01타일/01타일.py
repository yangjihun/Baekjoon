import sys
input = sys.stdin.readline

N = int(input())
d = { 0:0, 1:1, 2:2 }
for i in range(3,N+1):
  d[i%3] = (d[(i+1)%3]+d[(i+2)%3])%15746
print(d[N%3])