a = int(input())
plan = list(map(int,input().split()))
study = list(map(int,input().split()))
answer = 0
for i in range(a):
  if study[i]>=plan[i]:
    answer+=1
print(answer)