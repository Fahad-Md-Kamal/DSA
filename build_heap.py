# Adjust Heap
import random

def heapify(arr, length, item):

    largest = item
    left = 2 * item + 1
    right = 2 * item + 2
    
    if left < length and arr[left] > arr[largest]:
        largest = left
    
    if right < length and arr[right] > arr[largest]:
        largest = right

    print(f"largest: {largest}\n item: {item}\n")
    if largest != item:
        arr[item], arr[largest] = arr[largest], arr[item]

        heapify(arr, length, largest)



# Build Heap
def build_heap(arr):
    # non-leaf node to start
    arr_len = len(arr)
    startIdx = arr_len // 2 - 1

    for item in range(startIdx, -1, -1):
        heapify(arr, arr_len, item)

arr = []

for i in range(50):
    arr.append(random.randint(1, 111))

arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
print(arr)
build_heap(arr)
print('\n\n')
print(arr)