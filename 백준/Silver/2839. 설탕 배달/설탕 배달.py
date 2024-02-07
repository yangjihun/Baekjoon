def cul(n):
  if n==4 or n==7:
    return -1
  if (n%5)%3==0:
    return n//5 + n%5//3
  elif (n%5+5)%3==0:
    return n//5-1 + (n%5+5)//3
  elif (n%5+10)%3==0:
    return n//5-2 + (n%5+10)//3

N = int(input())
print(cul(N))