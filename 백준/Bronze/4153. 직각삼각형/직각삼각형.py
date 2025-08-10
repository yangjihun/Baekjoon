while(1):
    li = list(map(int,input().split()))
    a,b,c = sorted(li)
    if not (a or b or c):
        break
    if a**2 + b**2 == c**2:
        print('right')
    else:
        print('wrong')