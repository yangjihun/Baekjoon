T = int(input())

for _ in range(T):
  N,M = map(int,input().split())
  s = 1
  m = 1
  key = 1
  for i in range(M-N):
    s*=M-i
    m*=key
    key+=1
  print(s//m)