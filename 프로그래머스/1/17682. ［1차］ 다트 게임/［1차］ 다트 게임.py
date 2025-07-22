def solution(dartResult):
    scores = [] 
    i = 0
    
    while i < len(dartResult):
        # 1. 점수 추출 
        if dartResult[i] == '1' and i+1 < len(dartResult) and dartResult[i+1] == '0':
            score = 10
            i += 2
        else:
            score = int(dartResult[i])
            i += 1

        # 2. 보너스 처리
        if dartResult[i] == 'S':
            score = score ** 1
        elif dartResult[i] == 'D':
            score = score ** 2
        elif dartResult[i] == 'T':
            score = score ** 3
        i += 1

        # 3. 옵션 처리
        if i < len(dartResult) and dartResult[i] in ['*', '#']:
            if dartResult[i] == '*':
                score *= 2
                if scores:
                    scores[-1] *= 2 
            elif dartResult[i] == '#':
                score *= -1
            i += 1

        scores.append(score)

    return sum(scores)