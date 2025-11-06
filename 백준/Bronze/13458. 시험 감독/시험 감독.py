answer = int(input())
A = list(map(int,input().split()))
B,C = map(int,input().split())

for i in A:
    i-=B
    if i>0:
        answer += (i//C + (1 if i%C else 0))
print(answer)