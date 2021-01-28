import swap


def sort(integer_list):
    for i in range(0, len(integer_list)):
        jmin = i
        for j in range(i+1, len(integer_list)):
            if integer_list[j] < integer_list[jmin]:
                jmin = j
        if jmin != i:
            swap.swap(integer_list, i, jmin)
    return integer_list
