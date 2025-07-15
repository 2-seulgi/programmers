def solution(s):
    answer = []
    last_index = {} 

    for i, ch in enumerate(s):
        if ch in last_index:
            answer.append(i - last_index[ch])
        else:
            answer.append(-1)
        last_index[ch] = i
        
    return answer