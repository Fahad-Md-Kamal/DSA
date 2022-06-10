
solution = 0
for _ in range(int(input())):
    pl = list(map(int, input().split()))
    if pl.count(1)>1: solution += 1

print(solution)