def solution(num_list, n):
    start = num_list[:n]
    end = num_list[n:]
    answer = end + start
    return answer