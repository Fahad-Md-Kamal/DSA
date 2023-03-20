from generate_squence import give_a_list_to_sort

def merge_sort(arr):
    if len(arr) <= 1:
        return
    left_arr = arr[:len(arr)//2]
    right_arr = arr[len(arr)//2:]

    merge_sort(left_arr)
    merge_sort(right_arr)

    li = 0
    ri = 0
    ki = 0
    while li <len(left_arr) and ri < len(right_arr):
        if left_arr[li] < right_arr[ri]:
            arr[ki] = left_arr[li]
            li += 1
        else:
            arr[ki] = right_arr[ri]
            ri += 1
        ki += 1

    while li < len(left_arr):
        arr[ki] = left_arr[li]
        li += 1
        ki += 1

    while ri < len(right_arr):
        arr[ki] = right_arr[ri]
        ri += 1
        ki += 1


list_to_sort = give_a_list_to_sort()


print(list_to_sort)
merge_sort(list_to_sort)
print(list_to_sort)