import sys
input = sys.stdin.readline

S = [0]*21
M = int(input())

for _ in range(M):
  q = list(input().split())
  if q[0]=='add':
    S[int(q[1])] = 1
  elif q[0]=='check':
    print(S[int(q[1])])
  elif q[0]=='remove':
    S[int(q[1])] = 0
  elif q[0]=='toggle':
    S[int(q[1])] = 0 if S[int(q[1])] else 1
  elif q[0]=='all':
    S = [1 for i in range(21)]
  elif q[0]=='empty':
    S = [0 for _ in range(21)]
