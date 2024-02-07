def selection_sort(mas):
    sort_mas = []
    for _ in range(len(mas)):
        mn = mas[0]
        inx = 0
        for i in range(1, len(mas)):
            if mas[i] < mn:
                mn = mas[i]
                inx = i
        sort_mas.append(mn)
        mas[inx] = 10000
    return sort_mas