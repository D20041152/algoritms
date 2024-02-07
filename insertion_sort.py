def insertion_sort(mas):
    for i in range(len(mas) - 1):
        inx = i
        while mas[inx] > mas[inx + 1] and inx >= 0:
            mas[inx], mas[inx + 1] = mas[inx + 1], mas[inx]
            inx -= 1
    return mas
