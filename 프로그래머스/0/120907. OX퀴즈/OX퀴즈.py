def solution(quiz):
    answer = []
    
    for i in quiz:
        exp, result = i.split('=')
        if eval(exp.strip()) == int(result.strip()):
            answer.append("O")
        else:
            answer.append("X")
    return answer