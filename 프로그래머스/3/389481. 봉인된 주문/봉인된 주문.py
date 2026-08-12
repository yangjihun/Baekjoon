def str_to_num(s):
    num = 0
    for char in s:
        num = num * 26 + (ord(char) - ord('a') + 1)
    return num

def num_to_str(n):
    res = []
    while n > 0:
        n -= 1
        res.append(chr(ord('a') + (n % 26)))
        n //= 26
    return "".join(reversed(res))

def solution(n, bans):
    # 1. bans의 각 단어를 숫자로 변환 후 오름차순 정렬
    banned_nums = sorted([str_to_num(b) for b in bans])
    
    # 2. n 이하인 지워진 주문이 있을 때마다 n을 1씩 미룸
    for num in banned_nums:
        if num <= n:
            n += 1
        else:
            break
            
    # 3. 최종 n을 문자열로 변환하여 반환
    return num_to_str(n)