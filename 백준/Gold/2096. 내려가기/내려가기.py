import sys
input = sys.stdin.readline
mx = [0,0,0]
mn = [0,0,0]
for i in range(int(input())):
  a,b,c = map(int,input().split())
  mx = a + max(mx[0],mx[1]),b + max(mx),c + max(mx[1],mx[2])
  mn = a + min(mn[0],mn[1]),b + min(mn),c + min(mn[1],mn[2])
print(max(mx),min(mn))