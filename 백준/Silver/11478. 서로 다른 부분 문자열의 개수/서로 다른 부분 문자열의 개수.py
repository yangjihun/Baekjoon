S = input()
li = []

for i in range(len(S)):
  for j in range(i+1,len(S)+1):
    li.append(S[i:j])
print(len(set(li)))