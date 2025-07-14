def solution(s):
    answer = ''
    idx = 0  # 단어 내 인덱스

    for c in s:
        if c == ' ':
            answer += ' '
            idx = 0  
        else:
            if idx % 2 == 0:
                answer += c.upper()
            else:
                answer += c.lower()
            idx += 1  
    return answer
