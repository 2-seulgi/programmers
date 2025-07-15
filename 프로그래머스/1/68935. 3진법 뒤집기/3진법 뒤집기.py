def solution(n):
    answer = 0
    if n == 0:
        return "0"
    ternary =''
    while n > 0 :
        ternary = str(n%3) + ternary
        n //= 3
    
    s = str(ternary)[::-1]
    answer = int(s,3)
        
    return answer