from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None:
            return res
        queue = deque()
        queue.append(root)
        mark = {root}
        while queue:
            cur = queue.popleft()
            res.append(cur)
            for neighor in cur.neighours:
                if neighor not in mark:
                    queue.append(neighor)
                    mark.add(neighor)
        return res


