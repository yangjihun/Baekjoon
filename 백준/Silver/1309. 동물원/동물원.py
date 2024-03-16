N = int(input())

li = [1,3]
for _ in range(1,N):
  li.append((li[-1]*2+li[-2])%9901)

print(li[N])