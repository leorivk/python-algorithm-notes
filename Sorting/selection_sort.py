data = [1, 4, 3, 2, 7, 3]

'''
단순 선택 정렬 알고리즘의 원솟값을 비교하는 횟수 : n(n-1)/2 번

서로 이웃하지 않은 떨어져 있는 원소를 교환하므로 안정적이지 않다.
'''

def selection_sort(data):
    n = len(data)
    for i in range(n-1): # 정렬할 부분 중 가장 작은 원소의 인덱스
        for j in range(i+1, n):
            if data[j] < data[min]:
                min = j
        data[i], data[min] = data[min], data[i]
        