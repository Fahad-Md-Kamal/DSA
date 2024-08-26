def merge_sort(array):
    if len(array) <= 1:
        return array
    
    # Divide the array into two halves
    middle = len(array) // 2
    left_half = array[:middle]
    right_half = array[middle:]
    
    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_array = []
    left_index = 0
    right_index = 0
    
    # Merge the two sorted halves
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1
    
    # If there are any remaining elements in the left half, add them to the sorted array
    sorted_array.extend(left[left_index:])
    
    # If there are any remaining elements in the right half, add them to the sorted array
    sorted_array.extend(right[right_index:])
    
    return sorted_array

# Example usage
if __name__ == "__main__":
    sample_array = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", sample_array)
    sorted_array = merge_sort(sample_array)
    print("Sorted array:", sorted_array)
