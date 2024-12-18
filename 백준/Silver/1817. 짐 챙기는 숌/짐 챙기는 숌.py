import sys
input = sys.stdin.readline

n,m = map(int, input().split())
k = m
answer = 1
if n==0:
      answer = 0
else:
      for i in list(map(int, input().split())):
            if k - i < 0:
                  k = m
                  answer+=1
                  k -= i
            else:
                  k -= i
print(answer)