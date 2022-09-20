def even_odd(a):
    next_even, next_odd = 0, len(a) -1
    while next_even < next_odd:
        if a[next_even] % 2 == 0:
            next_even += 1
        else:
            a[next_even], a[next_odd] = a[next_odd], a[next_even]
            next_odd -= 1
    return a


arr_list = list(map(int, input().split(' ')))
print(even_odd(arr_list))
