data = [1, 4, 3, 2, 7, 3]

def qsort(data, left, right):
    pl = left
    pr = right
    x = data[(left + right) // 2]
    
    while pl <= pr:
        while data[pl] < x : pl += 1
        while data[pr] > x : pr -= 1
        
        if pl <= pr:
            data[pl], data[pr] = data[pr], data[pl]
            pl += 1
            pr -= 1
    
    if left < pr : qsort(data, left, pr)
    if right > pr : qsort(data, pl, right)
    
    
def pythonic_qsort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]

    left = [x for x in data[1:] if x <= pivot]
    right = [x for x in data[1:] if x > pivot]

    return qsort(left) + [pivot] + qsort(right)

