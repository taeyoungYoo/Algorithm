# 4256 트리
# 후위순회 : sub tree 모두 방문 후 root 방문

T = int(input())

def post_order(preorder: list, inorder: list):
    # 탈출 조건
    if not preorder:
        return
    # find root
    root_val = preorder[0]
    root_idx = inorder.index(root_val)
    post_order(preorder[1:root_idx+1], inorder[:root_idx])
    post_order(preorder[root_idx+1:], inorder[root_idx+1:])
    ret.append(root_val)
    
for _ in range(T):
    ret = []
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    post_order(preorder, inorder)
    for val in ret:
        print(val, end=' ')
    print()