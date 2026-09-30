def solution(numbers):
    answer = [-1] * len(numbers)
    stack = [0]
    idx = 1
    for i in range(len(numbers)):
        # 뒤에 있는 수가 더 크다면 청산
        while stack and numbers[i] > numbers[stack[-1]]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer