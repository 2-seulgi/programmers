def solution(number, limit, power):
    answer = 0
    d = []
    for i in range(1, number+1):
        count = 0
        for j in range(1, int(i**0.5)+1):
            if i % j == 0:
                if j == i // j:
                    count += 1
                else : 
                    count += 2
        if count <= limit :
            answer += count
        else:
            answer += power
            
    return answer