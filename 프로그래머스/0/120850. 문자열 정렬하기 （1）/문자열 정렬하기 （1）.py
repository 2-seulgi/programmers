def solution(my_string):
    digit_str = ''.join([c for c in my_string if c.isdigit()])
    answer =  [int(c) for c in digit_str]
    answer.sort()
    return answer