"""
 *packageName    : 
 * fileName       : 314. Binary Tree Vertical Order Traversal
 * author         : ipeac
 * date           : 2022-10-12
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-12        ipeac       최초 생성
 """
from collections import defaultdict, deque
from typing import List

import null as null

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verticalOrder(root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    
    columns = defaultdict(list)
    
    q = deque([(root, 0)])
    while q:
        node, x = q.popleft()
        columns[x].append(node.val)
        
        if node.left:
            q.append((node.left, x - 1))
        if node.right:
            q.append((node.right, x + 1))
    
    return [columns[x] for x in range(min(columns), max(columns) + 1)]

print(verticalOrder(root=[3, 9, 20, null, null, 15, 7]))
print(verticalOrder(root=[3, 9, 20, null, null, 15, 7]))
