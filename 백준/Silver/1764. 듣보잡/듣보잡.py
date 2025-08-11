import sys
input = sys.stdin.readline

N,M = map(int,input().strip().split())
set1 = set()
set2 = set()

for _ in range(N):
    set1.add(input().strip())

for _ in range(M):
    set2.add(input().strip())

result = sorted(list(set1 & set2))

print(len(result))
for i in result:
    print(i)