from generate_squence import give_a_list_to_sort


def quick_sort(sequence):
    if len(sequence) <= 1:
        return sequence
    
    pivot = sequence.pop()
    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
            
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

p = give_a_list_to_sort(20)
print(p)
res = quick_sort(p)
print(res)
