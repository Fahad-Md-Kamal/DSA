total_num = int(input())

# count = 1
# for i in range(1,total_num+1):
#     for j in range(total_num+1):
#         print(count, end=" ")
#         count +=1
#     print()


# for i in range(0,total_num+1):
#     r = i
#     for j in range(i):
#         print( r, end=" ")
#         r += 1
#     print()


"""
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1 
6 5 4 3 2 1 
7 6 5 4 3 2 1 
8 7 6 5 4 3 2 1 
"""

# for i in range(total_num):
#     for j in range(i+1):
#         print(i-j+1, end=" ")
#     print()

# for i in range(total_num):
#     """
#          *
#         **
#        ***
#       ****
#      *****
#     ******
#     """
#     for s in range(total_num-i):
#         print(" ", end="")

#     for j in range(i+1):
#         print('*', end= "")

#     print()


# for i in range(total_num):
#     """
#     ******
#     *****
#     ****
#     ***
#     **
#     *
#     """
#     for j in range(total_num-i):
#         print('*', end= "")

#     print()


# for i in range(total_num):
#     """
#     *****
#      ****
#       ***
#        **
#         *
#     """

#     for s in range(i):
#         print(' ', end= "")

#     for j in range(total_num-i):
#         print('*', end= "")

#     print()


for i in range(total_num):
    """
    *****
     ****
      ***
       **
        *
    """
    for s in range(total_num - i):
        print(' ', end= "")

    for j in range(1, i+1):
        print(j, end= "")
    
    for s in range(i-1,-1):
        print(s, end= "")
        
    # for k in range(1, i):
    #     print(total_num-i-k, end= " ")

    print()