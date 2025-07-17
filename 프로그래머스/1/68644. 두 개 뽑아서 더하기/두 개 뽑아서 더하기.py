def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in range(i+1 , len(numbers)):

            print(numbers[i]+numbers[j])
            answer.add(numbers[i]+numbers[j])
                     
    return sorted(answer)