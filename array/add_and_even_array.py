given_list = [1, 2, 3, 4, 5, 6, 66, 9, 11, 22, 44, 33]

next_even = 0
next_odd = len(given_list) - 1

while next_even < next_odd:
    if given_list[next_even] % 2 == 0:
        next_even += 1
    else:
        given_list[next_even], given_list[next_odd] = given_list[next_odd], given_list[next_even]
        next_odd -= 1

print(given_list)