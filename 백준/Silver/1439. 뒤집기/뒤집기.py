n = input()
s = n[0]
result = 0

for i in n[1:]:
  if s!=i:
    result+=1
    s = i
print(result//2+result%2)