T = int(input())

for _ in range(T):
    a = [1,0,1]
    num = int(input())
    for i in range(2,num+2):
        a[i%3] = a[(i-1)%3] + a[(i-2)%3]
    print(a[(num)%3], a[(num+1)%3])