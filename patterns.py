def star_square(n:int):
    """
    * * *
    * * *
    * * *
    """
    for i in range(1, n):
        for j in range(1, n):
            print(j, end=" ")
        print()


def char_square_1(n:int):
    """
    a a a a a 
    b b b b b 
    c c c c c 
    d d d d d 
    e e e e e 
    """
    for i in range(1, n):
        for j in range(1, n):
            print(chr(96+i), end=" ")
        print()


def char_square_2(n:int):
    """
    A A A A A 
    B B B B B 
    C C C C C 
    D D D D D 
    E E E E E 
    """
    for i in range(1, n):
        for j in range(1, n):
            print(chr(64+i), end=" ")
        print()


def char_square_3(n:int):
    """
    a A a A a A a A a A 
    b B b B b B b B b B 
    c C c C c C c C c C 
    d D d D d D d D d D 
    e E e E e E e E e E 
    """
    for i in range(1, n):
        for j in range(1, n):
            print(chr(96+i), end=" ")
            print(chr(64+i), end=" ")
        print()


def char_square_4(n:int):
    """
    a a a
    B B B
    c c c
    """
    for i in range(1, n):
        for j in range(1, n):
            print(chr(64+i), end=" ") if i%2==0 else print(chr(96+i), end=" ")
        print()

def num_square_1(n:int):
    """
    1 1 1 1 
    2 2 2 2 
    3 3 3 3 
    4 4 4 4
    """ 
    for i in range(1, n):
        for j in range(1, n):
            print(i, end=" ")
        print()


def num_square_2(n: int):
    """
    1 1 1 1 1
    1 1 1 2 2
    1 1 3 3 3
    1 4 4 4 4
    5 5 5 5 5
    """
    for r in range(1,n):
        for c in range(1, n):
            if c<=n-r:
                print(1, end=" ")
            else:
                print(r, end=" ")
        print()


def star_char_square_1(n: int):
    """
    * * * * *
    * A B C *
    * D E F *
    * G H I *
    * * * * *
    """
    ch = ord("A")
    val = 0
    for r in range(1,n+1):
        for c in range(1, n+1):
            if r==1 or c==1 or r ==n or c == n:
                print("*", end=" ")
            else:
                char = chr(ch+val)
                print(char, end=" ")
                if char == "Z":
                    ch = ord("A")
                    val = -1
                val += 1
        print()


def left_piramid_decriment(n: int):
    """
    *
    * *
    * * *
    * * * *
    * * * * *
    """
    for r in range(n+1):
        for _ in range(0,r):
            print("* ", end="")
        print()


def left_piramid_incriment(n: int):
    """
    * * * * * * 
    * * * * * 
    * * * * 
    * * * 
    * * 
    *
    """
    for r in range(n, 0, -1):
        for _ in range(r, 0, -1):
            print("* ", end="")
        print()

def num_left_piramid_decriment(n: int):
    """
    1
    2 1
    3 2 1
    4 3 2 1
    5 4 3 2 1
    """
    for r in range(n+1):
        row = r
        for c in range(0,r):
            print(row, end="")
            row -= 1
        print()
    

def num_seq_left_piramid_dec(n: int):
    """
    1 
    2 3 
    4 5 6 
    7 8 9 10 
    11 12 13 14 15
    """
    num = 1
    for r in range(n+1):
        for c in range(0,r):
            print(num, end=" ")
            num += 1
        print()

def signed_pattern(n: int):
    """
    *
    $ *
    * $ *
    $ * $ *
    * $ * $ *
    """
    for r in range(n+1):
        for c in range(0,r):
            print('*', end=" ") if (r+c)%2 == 0 else print('$', end=" ")
        print()


def char_num_comb_pattern(n: int):
    """
    A
    1 1
    B B B
    2 2 2 2
    C C C C C
    """
    nu = 1
    al = 1
    for r in range(1, n+1):
        for c in range(0,r):
            if r%2 == 0:
                print(nu, end=" ")
            else:
                print(chr(64+al), end=" ")
        if r%2 == 0:
            nu +=1
        else:
            al +=1
        print()

def right_piramid(n: int):
    """
        *
       **
      ***
     ****
    *****
    """
    for r in range(n):
        for s in range(0, n-r):
            print(" ", end="")
        for c in range(0, r+1):
            print("*", end="")
        print()

def piramid(n: int):
    """
        *
       * *
      * * *
     * * * *
    * * * * *
    """
    for r in range(n):
        for s in range(0, n-r):
            print(" ", end="")
        for c in range(0, r+1):
            print("* ", end="")
        print()

def hypended_piramid(n: int):
    """
        *
       * *
      * * *
     * * * *
    * * * * *
    """
    for r in range(n):
        for s in range(1, n-r):
            print("- ", end="")
        for c in range(0, r+1):
            print("* ", end="")
        print()


if __name__=="__main__":
    num = int(input("Enter number of rows: "))
    # star_square(5)
    # num_square_1(5)
    # char_square_1(6)
    # char_square_2(6)
    # char_square_3(6)
    # char_square_4(6)
    # num_square_1(6)
    # num_square_2(6)
    # star_char_square_1(num)
    # left_piramid_decriment(num)
    # left_piramid_incriment(num)
    # num_left_piramid_decriment(num)
    # num_seq_left_piramid_dec(num)
    # signed_pattern(num)
    # char_num_comb_pattern(num)
    # right_piramid(num)
    # piramid(num)
    hypended_piramid(num)
