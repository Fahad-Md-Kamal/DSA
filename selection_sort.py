from generate_squence import give_a_list_to_sort

def selection_sort(seq: list):
    for i in range(len(seq)):
        curr_min = i

        for j in range(i+1, len(seq)):
            if seq[j] < seq[curr_min]:
                curr_min = j

        seq[i], seq[curr_min] = seq[curr_min], seq[i]

lts = give_a_list_to_sort(30)
print(lts)
selection_sort(lts)

print(lts)