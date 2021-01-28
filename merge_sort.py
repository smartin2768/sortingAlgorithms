def sort(integer_list):
    length = len(integer_list)
    if length <= 1:
        return integer_list

    left = integer_list[0:int(length/2)]
    right = integer_list[int(length/2):length]
    print(f"Split list \n l: {left} \n r: {right}")

    left = sort(left)
    print(f"{left}")
    right = sort(right)
    print(f"{right}")

    return merged(left, right)


def merged(left, right):
    result = []
    while not left == [] and not right == []:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if not left == []:
        result.extend(left)
    elif not right == []:
        result.extend(right)
    return result
