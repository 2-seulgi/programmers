def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        slice = array[i-1:j]
        slice.sort()
        s = slice[k-1]
        answer.append(s)
    return answer