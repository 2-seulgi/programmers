def solution(my_string):
    answer = 0
    digits = [int(c) for c in my_string if c.isdigit()]
    for i in digits:
        answer += i
    
    return answer