import swap


def sort(integer_list):
    print(f"We're doing a Bubble Sort")
    length_of_list = len(integer_list)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, length_of_list-1):
            if integer_list[i-1] > integer_list[i]:
                integer_list = swap.swap(integer_list, i-1, i)
                swapped = True
    return integer_list