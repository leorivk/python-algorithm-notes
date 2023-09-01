data = [1, 4, 3, 2, 7, 3]

for i in range(len(data)):
    min_index = i
    for j in range(i+1, len(data)):
        if data[j] < data[min_index]:
            min_index = j
    data[min_index], data[i] = data[i], data[min_index]
    
print(data)