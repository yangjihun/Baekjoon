li = [0,0,0]
for i in range(int(input())):
  rgb = list(map(int,input().split()))
  li = [rgb[0]+min(li[1],li[2]),rgb[1]+min(li[0],li[2]),rgb[2]+min(li[0],li[1])]
print(min(li))