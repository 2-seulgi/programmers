def solution(x):
    answer = True
    n = 0
    for i in str(x):
        n += int(i)
    if x % n == 0:
        answer = True
    else:
        answer = False
    return answer