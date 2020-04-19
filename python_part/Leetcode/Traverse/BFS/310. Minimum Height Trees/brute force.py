from typing import List
'''
暴力法，不大行。结果虽然是正确的，复杂度太高
让所有node都当一遍head，并进行一次BFS，求树的长度。最后在筛选

'''
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # adj_list
        adj_list = {_: set() for _ in range(n)}
        for n1, n2 in edges:
            adj_list[n1].add(n2)
            adj_list[n2].add(n1)
        min_level, min_head = float("inf"), []
        # 每个node都做一遍head
        for head in range(n):
            cur_level = [head]
            marked = {head}
            level = 1
            # 开始简易版BFS，记录level
            while cur_level:
                next_level = []
                level += 1
                for cur in cur_level:
                    for next_node in adj_list[cur]:
                        if next_node not in marked:
                            next_level.append(next_node)
                            marked.add(next_node)
                cur_level = next_level
            # 判定大小，处理数据
            if level == min_level:
                min_head.append(head)
            elif level < min_level:
                min_head = [head]
                min_level = level

        return min_head


foo = Solution()
print(foo.findMinHeightTrees(4,[[1,0],[1,2],[1,3]]))
