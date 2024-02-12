def sheel_sort(mas):
    n = len(mas)
    step = n // 2
    while step > 0:
        for i in range(step, n):
            inx = i
            while mas[inx - step] > mas[inx] and inx - step >= 0:
                mas[inx - step], mas[inx] = mas[inx], mas[inx - step]
                inx -= step
        step //= 2

    return mas