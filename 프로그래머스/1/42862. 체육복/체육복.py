def solution(n, lost, reserve):
    # 도난도 당하고 여벌도 있는 사람 제거
    lost_set = [l for l in lost if l not in reserve]
    reserve_set = [r for r in reserve if r not in lost]

    for r in sorted(reserve_set):
        if r - 1 in lost_set:
            lost_set.remove(r - 1)
        elif r + 1 in lost_set:
            lost_set.remove(r + 1)

    return n - len(lost_set)