def solution(a, b):
    answer = ''
    count = 0
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    # 월별 일 수를 배열로 정의 (2016년은 윤년)
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(1, a):
        count += month_days[i-1]
        
    count += b
    
    day = (count + 4) % 7 
    answer = days[day]
    
    return answer