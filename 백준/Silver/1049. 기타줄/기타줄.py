N,M = map(int,input().split())
package = []
na = []
min_in_package = 1000000
min_in_na = 1000000
mini = 1000000
for _ in range(M):
  a,b = map(int,input().split())
  package.append(a)
  na.append(b)


#1
for i in package:
  if (1+N//6)*i<min_in_package:
    min_in_package = (1+N//6)*i

#2
for i in na:
  if i*N<min_in_na:
    min_in_na = i*N

#3
for i in package:
  for j in na:
    if (N//6)*i+(N%6)*j<mini:
      mini = (N//6)*i+(N%6)*j

print(min(mini,min_in_na,min_in_package))