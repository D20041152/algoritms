def quick_sort(mas):
    if len(mas) < 2:
        return mas
    key_elem = mas[0]
    less = [elem for elem in mas[1:] if elem < key_elem]
    gress = [elem for elem in mas[1:] if elem >= key_elem]
    return quick_sort(less) + [key_elem] + quick_sort(gress)
