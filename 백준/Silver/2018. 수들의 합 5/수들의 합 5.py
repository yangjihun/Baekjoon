N = int(input())
start_point = 1
end_point = 1
count = 1
sum = 1

while end_point!=N:
  if sum < N:
    end_point+=1
    sum+=end_point
  elif sum > N:
    sum-=start_point
    start_point+=1
  elif sum==N:
    end_point+=1
    sum+=end_point
    count+=1
print(count)