while 1:
  num = int(input())
  num_list = []
  if num==-1:
    break
  for i in range(1,num//2+1):
    if num%i==0:
      num_list.append(i)
  if sum(num_list)==num:
    print(num,'=',end=' ')
    for i in num_list:
      if i!=num_list[-1]:
        print(i,'+',end=' ')
      else:
        print(i)
  else:
    print(num,'is NOT perfect.')