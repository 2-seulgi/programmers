def solution(sizes):
    sizes = [sorted(x, reverse = True) for x in sizes]
    max_width = max(x[0] for x in sizes)
    max_heigh = max(x[1] for x in sizes)
    
    return max_width * max_heigh