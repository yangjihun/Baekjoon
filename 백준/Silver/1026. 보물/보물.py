N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
B_index = sorted(B)[::-1]
result = 0
A.sort()
for i in range(N):
  result += A[i]*B_index[i]
print(result)