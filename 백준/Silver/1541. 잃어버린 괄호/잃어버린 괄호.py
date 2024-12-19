s = input()
n = 0
answer = 0
k = ''
for i in s:
  if i=='-':
    answer += int(k) if n==0 else -int(k)
    k = ''
    n = 1
  elif i=='+':
    answer += int(k) if n==0 else -int(k)
    k = ''
  else:
    k+=i
answer += int(k) if n==0 else -int(k)
print(answer)