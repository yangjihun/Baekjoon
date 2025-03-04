import sys
input = sys.stdin.readline

N = int(input())
table = []

for _ in range(N):
  age,name = input().split()
  table.append([int(age),name])

table.sort(key = lambda x : x[0])

for i in table:
  print(i[0],i[1])