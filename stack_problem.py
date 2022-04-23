from stack_data_stracture import Stack


def is_match(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    return False

def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "({[":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False


def div_by_2(dec_num):
    s = Stack()
    while dec_num > 0:
        reminder = dec_num % 2
        s.push(reminder)
        dec_num = dec_num // 2
        # print(dec_num, end='')
    # print(s.get_stack())

    bin_num = ''
    while not s.is_empty():
        bin_num += str(s.pop())
    
    return bin_num
    

if __name__ == '__main__':
    print(div_by_2(242))
    print(div_by_2(242) == bin(242)[2:])
    # print(is_paren_balanced('()'))
    div_by_2(242)