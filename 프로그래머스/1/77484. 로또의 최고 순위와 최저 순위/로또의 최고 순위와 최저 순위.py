def solution(lottos, win_nums):
    equals = 0
    gap = 0
    for i in lottos:
        if i == 0:
            gap += 1
            continue
        if i in win_nums:
            equals += 1
    min_rank = 7 - equals if equals > 0 else 6
    max_rank = 7 - (equals + gap) if (equals + gap) > 0 else 6
    return [max_rank, min_rank]
    raise NotImplementedError("TODO: solve the problem")
