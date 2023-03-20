from generate_squence import give_a_list_to_sort

def bubble_sort(seq:list):
    for i in range(len(seq)):
        for j in range(len(seq) - i - 1):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]

seq = give_a_list_to_sort(9000)
bubble_sort(seq)
