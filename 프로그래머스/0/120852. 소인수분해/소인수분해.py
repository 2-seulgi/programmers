def solution(n):
    answer = []
    i = 2
    while (n != 1):
        if n % i == 0:
            if i not in answer:
                answer.append(i)
            n //= i
        else:
            i += 1
            
    return answer