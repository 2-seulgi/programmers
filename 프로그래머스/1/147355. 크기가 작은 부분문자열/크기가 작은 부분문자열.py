def solution(t, p):
    answer = 0
    for i in range(0, len(t)-len(p)+1):
        s = t[i : i+len(p)]
        if int(s) <= int(p):
            print(s)
            answer +=1
    return answer