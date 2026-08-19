def solution(info, edges):
    answer = 0
    def dfs(curr, li, sheep, wolf):
        nonlocal answer
        if info[curr]:
            wolf += 1
        else:
            sheep += 1
        if wolf >= sheep:
            return
        answer = max(answer, sheep)
        # li 최신화
        new_li = list(li)
        new_li.remove(curr)
        new_li.extend(nodes[curr])
        
        for node in new_li:
            dfs(node, new_li, sheep, wolf)
    
    nodes = [[] for _ in range(len(info))]
    for node in edges:
        nodes[node[0]].append(node[1])
    # dfs
    dfs(0, [0], 0, 0)
    
    return answer