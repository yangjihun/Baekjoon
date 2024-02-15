S = input()
data = ''
key = 0
result = ''
for i,k in enumerate(S):
  if key==0:
    if k==' ':
      result+=(data[::-1]+' ')
      data = ''
    elif k=='<':
      result+=(data[::-1])
      data = '<'
      key = 1
    else:
      data+=k
  elif key==1:
    if k=='>':
      result+=(data+'>')
      key = 0
      data = ''
    else:
      data+=k
if data:
  result = result+data[::-1]
print(result)