def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    sample_array = [3, 9, 10, 27, 38, 43, 82]
    print("Array:", sample_array)
    sorted_array = binary_search(sample_array, 82)
    print("Target index:", sorted_array)
