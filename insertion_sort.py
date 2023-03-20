from generate_squence import give_a_list_to_sort


def insertion_sort(seq:list):
    for i in range(len(seq)):
        while seq[i-1] > seq[i] and i > 0:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i -= 1

l_t_s = give_a_list_to_sort(1000)
print(l_t_s)
insertion_sort(l_t_s)
print(l_t_s)
    