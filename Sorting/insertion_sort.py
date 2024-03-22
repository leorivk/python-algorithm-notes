data = [1, 4, 3, 2, 7, 3]

'''
서로 떨어져 있는 원소를 교환하지 않으므로 안정적

원소의 비교 횟수 : n^2/2
'''

def insertion_sort(data):
    n = len(data)
    
    for i in range(1, n):
        target = data[i]
        j = i
        
        '''
        - 종료 조건 1 : 정렬된 배열의 왼쪽 끝에 도달한 경우
        - 종료 조건 2 : target보다 작거나 같은 data[j-1]를 발견한 경우
        
        드모르간 법칙
        - 계속 조건 1 : j가 0보다 큰 경우
        - 계속 조건 2 : data[j-1]가 target보다 큰 경우
        '''
        
        while j > 0 and data[j-1] > target:
            data[j] = data[j-1]
            j -= 1
        
        data[j] = target