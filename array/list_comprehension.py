# Merging 2 Array
A = [1,3, 5]
B = ['a', 'b', 'c']
result = [(x,y) for x in A for y in B] 
print(result) #[(1, 'a'), (1, 'b'), (1, 'c'), (3, 'a'), (3, 'b'), (3, 'c'), (5, 'a'), (5, 'b'), (5, 'c')]

# --------------------------------------------------------

# 2D array ==> 1D array
M = [['a', 'b', 'c'], ['d', 'e', 'f']]
merged_arr = [x for row in M for x in row]
print(merged_arr) # ['a', 'b', 'c', 'd', 'e', 'f']

# --------------------------------------------------------

# squre each item of 2D arr
N = [[1,2,3], [4,5,6]]
squre_result = [[x**2 for x in row] for row in N]
print(squre_result)

# --------------------------------------------------------

# squre each item of 2D arr And Merge
N = [[1,2,3], [4,5,6]]
squre_merge_result = [ x** 2 for row in N for x in row]
print(squre_merge_result)