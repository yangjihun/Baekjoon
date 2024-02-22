grades = {
  'A+':4.5,
  'A0':4,
  'B+':3.5,
  'B0':3,
  'C+':2.5,
  'C0':2,
  'D+':1.5,
  'D0':1,
  'F':0
  }
result = 0
num = 0

for _ in range(20):
  a,b = input().split()[1:]
  if b!='P':
    num+=float(a)
    result += float(a)*grades[b]

print(result/num)