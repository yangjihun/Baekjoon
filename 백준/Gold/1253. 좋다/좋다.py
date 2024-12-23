N = int(input())
li = sorted(list(map(int,input().split())))
answer = 0

for i in range(N):
  s = 0
  e = N-1
  while s<e:
    if li[s]+li[e]==li[i]:
      if i!=s and i!=e:
        answer+=1
        break
      elif i==s:
        s+=1
      elif i==e:
        e-=1
    elif li[s]+li[e]>li[i]:
      e-=1
    else:
      s+=1
print(answer)