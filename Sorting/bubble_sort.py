data = [1, 6, 4, 3, 7, 2, 9, 8, 5]

def general_bubble_sort(data):
    n = len(data)

    # 오름차순 정렬
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if data[j] < data[j-1]:
                data[j], data[j-1] = data[j-1], data[j]
                
    print(data)

    '''
    버블 정렬은 1칸 이상 떨어져 있는 원소를 교환하는 것이 아니라,
    서로 이웃한 원소만 교환하므로 안정적이다.

    원소를 비교하는 횟수는 첫 번째 루프에서는 n-1, 두 번째 루프에서는 n-2, ... 이므로
    합계는 다음과 같다.

    (n+1) + (n+2) + ... + 1 = n(n-1)/2

    하지만 실제 횟수는 배열의 원솟값에 따라 영향을 받으므로 평균값은 그의 절반인 n(n-1)/4번이다.
    '''

def improved_bubble_sort_1(data):
    '''
    이미 정렬이 되어 있는 상태라면 이후 루프부터는 원소 교환이 이루어지지 않는다.
    만약 교환이 이루어지지 않는다면 정렬을 종료시켜 실행 시간을 단축시킬 수 있다.
    '''
    
    n = len(data)
    
    for i in range(n-1):
        ex_cnt = 0 # 해당 루프에서의 교환 횟수
        for j in range(n-1, i, -1):
            if data[j] < data[j-1]:
                data[j], data[j-1] = data[j-1], data[j]
                ex_cnt += 1
            
        if ex_cnt == 0:
            break
        
def improved_bubble_sort_1(data):
    '''
    루프마다 비교, 교환을 수행하다가 특정 원소 이후부터 교환이 이루어지지 않는다면
    해당 원소의 앞쪽에 있는 원소들은 이미 정렬이 되어 있다는 것을 의미한다.
    이미 정렬이 된 앞 부분은 제외한 후 비교, 교환을 한다면 시간을 단축 시킬 수 있다.
    '''
    n = len(data)
    
    k = 0
    
    while k < n-1:
        last = n-1
        for i in range(n-1, k, -1):
            if data[i] < data[i-1]:
                data[i], data[i-1] = data[i-1], data[i]
                last = i
        k = last

def shaker_sort(data):
    n = len(data)
    
    left = 0
    right = n-1
    
    last = right
    
    while left < right:
        for i in range(right, left, -1):
            if data[i] < data[i-1]:
                data[i], data[i-1] = data[i-1], data[i]
                last = i
        left = last
        
        for i in range(left, right):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1] = data[i]
                last = i
        right = last