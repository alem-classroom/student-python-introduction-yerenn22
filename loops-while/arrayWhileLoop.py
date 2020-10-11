def insert_squares(arr, num):
    i = 1
    while (i != num + 1):
        arr.append(i * i)
        i += 1
    return arr
