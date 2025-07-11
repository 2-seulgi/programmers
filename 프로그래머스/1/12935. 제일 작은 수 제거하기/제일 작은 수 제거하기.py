def solution(arr):
    answer = arr
    remove_set = sorted(arr)  
    if len(answer) == 1:
        answer = [-1]
    else:
        answer.remove(remove_set[0])

    return answer