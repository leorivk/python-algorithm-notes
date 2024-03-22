'''
선형 검색의 종료 조건
1. i == len(data)가 성립할 때
2. data[i] == x 가 성립했을 때
'''

def while_linear_search(data, x):
    i = 0
    
    while True:
        if i == len(data):
            return -1
        if data[i] == x:
            return i
        i += 1

def for_linear_search(data, x):
    for i in range(len(data)):
        if data[i] == x:
            return i
    return -1

def sentinel_linear_search(data, x):
    '''
    보초법을 사용하면 선형 검색의 종료 조건 중 1번 조건을 확인하지 않아도 된다.
    '''
    data.append(x)
    
    i = 0
    
    while True:
        if data[i] == x:
            return i
        i += 1