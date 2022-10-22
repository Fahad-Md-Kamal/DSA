def dnf(A: list, pivot: int):
    p1, equal, p2 = 0, 0, len(A) -1

    pivot_num = A[pivot]

    while equal <= p2:
        if A[equal] == pivot_num:
            equal += 1
        elif A[equal] < pivot_num:
            A[p1], A[equal] = A[equal], A[p1]
            p1 += 1
            equal += 1
        else:
            A[p2], A[equal] = A[equal], A[p2]
            p2 -= 1
            equal += 1


arr = [1,2, 1, 0, 2, 1, 0, 2]
dnf(arr, 4)
print(arr)