def shell_sort(mas):
    n = len(mas)
    step = n // 2

    while step > 0:
        for i in range(step, n):
            temp = mas[i]
            j = i
            while j - step >= 0 and mas[j - step] > temp:
                mas[j] = mas[j - step]
                j -= step
            mas[j] = temp
        step //= 2
    return mas