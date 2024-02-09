N = int(input())
li = []
result = ''
for _ in range(N):
  li.append(input())

for i in li:
  if i[::-1] in li:
    result = i
    break
print(len(result), result[len(result)//2])