N = int(input())
li = list(map(int,input().split()))
answer = [1] * N

for i in range(N):
    for j in range(i):
        if li[i]>li[j]:
            answer[i] = max(answer[i],answer[j]+1)
print(max(answer))