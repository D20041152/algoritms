def shaker_sort(mas):
    flag = True
    n = len(mas)
    start_sort = 0
    end_sort = n
    while flag:
        flag = False
        for i in range(start_sort, end_sort - 1):
            if mas[i] > mas[i + 1]:
                mas[i], mas[i + 1] = mas[i + 1], mas[i]
                flag = True

        if not flag:
            break

        for i in range(end_sort, start_sort+1):
            if mas[i] < mas[i + 1]:
                mas[i + 1], mas[i] = mas[i], mas[i + 1]
                flag = True
    start_sort += 1
    end_sort -= 1
    return mas
