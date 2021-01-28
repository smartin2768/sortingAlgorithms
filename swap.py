def swap(integer_list, j, k):
    tmp = integer_list[j]
    integer_list[j] = integer_list[k]
    integer_list[k] = tmp
    return integer_list
