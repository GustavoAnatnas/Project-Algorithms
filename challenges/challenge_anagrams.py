# https://stackoverflow.com/questions/18761766/mergesort-with-python
# ideia de merge e merge_sort retirada do StackOverflow
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    return merge(left_arr, right_arr)


def merge(left_arr, right_arr):
    result = []
    i = j = 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(right_arr[j])
            j += 1

    result += left_arr[i:]
    result += right_arr[j:]

    return result


def is_anagram(first_str, second_str):
    if not first_str and not second_str:
        return tuple(("", "", False))

    first_str = first_str.lower().replace(" ", "")
    second_str = second_str.lower().replace(" ", "")

    first_list = list(first_str)
    second_list = list(second_str)

    first_list = merge_sort(first_list)
    second_list = merge_sort(second_list)

    if first_list == second_list:
        return tuple(("".join(first_list), "".join(second_list), True))
    else:
        return tuple(("".join(first_list), "".join(second_list), False))
