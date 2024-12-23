n = int(input())
li = []
ans = []
answer = ''
i = 1
for _ in range(n):
  ans.append(int(input()))
  while ans[-1]>=i:
    li.append(i)
    i+=1
    answer+='+'
  if li[-1]==ans[-1]:
    li.pop()
    ans.pop()
    answer+='-'
if li==[]:
  for i in answer:
    print(i)
else:
  print("NO")