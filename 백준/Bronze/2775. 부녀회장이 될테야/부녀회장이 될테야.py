for _ in range(int(input())):
  k = int(input())
  n = int(input())
  li = [[x for x in range(1,n+1)] for _ in range(k+1)]
  for i in range(1,len(li)):
    for j in range(1,n):
      li[i][j] = sum(li[i-1][:j+1])
  print(li[-1][-1])