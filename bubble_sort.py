def bubble_sort(mas):
    for i in range(len(mas)):
        for j in range(len(mas)-i-1):
            if mas[j] > mas[j+1]:
                mas[j], mas[j+1] = mas[j+1], mas[j]

    return mas
