import swap


def sort(integer_list):
    return quick_sort(integer_list, 0, len(integer_list)-1)


def quick_sort(integer_list, lo, hi):
    if lo < hi:
        partition_point = partition(integer_list, lo, hi)
        quick_sort(integer_list, lo, partition_point)
        quick_sort(integer_list, partition_point+1, hi)
    return integer_list


def partition(integer_list, lo, hi):
    mid = integer_list[int((lo + hi)/2)]
    i = lo
    j = hi
    while True:
        while integer_list[i] < mid:
            i = i + 1
        while integer_list[j] > mid:
            j = j - 1
        if i >= j:
            return j
        swap.swap(integer_list, i, j)