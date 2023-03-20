from random import randint


def give_a_list_to_sort(items:int = 50):
    return [randint(0, 999) for _ in range(items)]
