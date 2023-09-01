data = [0, 2, 5, 2, 3, 9, 3]

def counting_sort(data):
    count = [0] * (max(data) + 1)

    for i in data:
        count[i] += 1

    sorted_arr = []

    for i in range(len(count)):
        for _ in range(count[i]):
            sorted_arr.append(i)

    print(sorted_arr)

counting_sort(data)