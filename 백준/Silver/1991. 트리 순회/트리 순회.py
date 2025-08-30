N = int(input())
tree = {}
for i in range(N):
    node, l_child_node, r_child_node = input().split()
    tree[node] = [l_child_node, r_child_node]

def preorder(n):
    if n!='.':
        print(n, end='')
        preorder(tree[n][0])
        preorder(tree[n][1])

def inorder(n):
    if n!='.':
        inorder(tree[n][0])
        print(n, end='')
        inorder(tree[n][1])

def postorder(n):
    if n!='.':
        postorder(tree[n][0])
        postorder(tree[n][1])
        print(n, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')