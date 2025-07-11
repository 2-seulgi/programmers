def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):  # 행 인덱스
        row = []
        for j in range(len(arr1[0])):  # 열 인덱스
            row.append(arr1[i][j] + arr2[i][j])
        answer.append(row)
    return answer
