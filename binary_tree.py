class Node:

    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
    
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

def depth_first_values(root):
    """
    DFS Iterative
    """
    if root == None: return []
    result = []
    stack = [root]
    while len(stack) > 0:
        current = stack.pop()
        result.append(current.val)

        if current.right: stack.append(current.right)
        if current.left: stack.append(current.left)
    return result

def depth_first_values_recursive(root):
    """
    DFS Recursive
    """
    if root == None: return []

    left_values = depth_first_values_recursive(root.left)
    right_values = depth_first_values_recursive(root.right)

    return [root.val, *left_values, *right_values]


def bredth_first_values(root):
    """
    BFS Iterative
    """
    if root == None: return []
    result = []
    stack = [root]
    while len(stack) > 0:
        current = stack.pop(0)
        result.append(current.val)

        if current.left: stack.append(current.left)
        if current.right: stack.append(current.right)
    return result


if __name__ == '__main__':
    # result = depth_first_values(a)
    # print(' '.join(result))

    # result = depth_first_values_recursive(a)
    # print(' '.join(result))

    result = bredth_first_values(a)
    print(' '.join(result))
