def solution(name, yearning, photo):
    answer = []
    score_map = dict(zip(name,yearning ))
    for friends in photo:
        total = 0
        for person in friends:
            if person in score_map:
                total += score_map[person]
        answer.append(total)
            
        
    return answer