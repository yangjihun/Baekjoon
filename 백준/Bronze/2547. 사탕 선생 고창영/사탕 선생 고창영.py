T = int(input())
count = 0
while count!=T:
  candy = 0
  if (input()==''):
    student = int(input())
    for i in range(student):
      candy+=int(input())
    if candy%student:
      print('NO')
    else:
      print('YES')
    count+=1
