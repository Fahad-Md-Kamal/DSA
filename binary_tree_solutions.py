class Node:

    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')

a = Node(100)
b = Node(200)
c = Node(300)
d = Node(4)
e = Node(500)
f = Node(60)
g = Node(70)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
# c.left = g

def tree_include_iter_BFS(root, target):
    """
    BFS Iterative
    """
    if root == None: return []
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        if current.val == target: return True
        if current.left: queue.append(current.left, target)
        if current.right: queue.append(current.right, target)
    return False

# print(tree_include_iter_BFS(a, 'k'))

def tree_include_recur_DFS(root, target):
    """
    DFS Recursive
    """
    if root == None: return False
    if root.val == target: return True
    return tree_include_recur_DFS(root.left, target) or tree_include_recur_DFS(root.right, target)

# print(tree_include_recur_DFS(a, 'a'))


def tree_sum_recur_DFS(root):
    """
    DFS Recursive
    """
    if root == None: return 0
    return root.val + tree_sum_recur_DFS(root.left) + tree_sum_recur_DFS(root.right)

# print(tree_sum_recur_DFS(a))


def tree_min_iter_DFS(root):
    """
    BFS Iterative
    """
    smallest = float('inf')
    stack = [root]
    while len(stack) > 0:
        current = stack.pop()
        smallest = min(smallest, current.val)

        if current.left: stack.append(current.left)
        if current.right: stack.append(current.right)
    return smallest

# print(tree_min_iter_DFS(a))


def tree_min_iter_BFS(root):
    """
    BFS Iterative
    """
    smallest = float('inf')
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        smallest = min(smallest, current.val)

        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
    return smallest

# print(tree_min_iter_BFS(a))


def tree_min_recur_BFS(root):
    """
    BFS Recursive
    """
    if root == None: return float('inf')
    return min(root.val , tree_min_recur_BFS(root.left) , tree_min_recur_BFS(root.right))

# print(tree_min_recur_BFS(a))


def tree_max_recur(root):
    if root == None: return float('-inf')
    if root.left == None and root.right == None: return root.val
    max_child = max(tree_max_recur(root.left) , tree_max_recur(root.right))
    return root.val + max_child

# print(tree_max_recur(a))
