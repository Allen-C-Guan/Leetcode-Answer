from typing import List
'''
Topology sort
'''
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adj_list and in_degree
        adj_list = [set() for _ in range(numCourses)]
        in_degree = {i: 0 for i in range(numCourses)}

        for course, pre_course in prerequisites:
            adj_list[pre_course].add(course)
            in_degree[course] += 1

        queue, res = deque(), []
        # 压入heads，  所有in——degree的都可以作为BFS的头，多线同时开始
        for i in range(numCourses):
            if not in_degree[i]: queue.append(i)

        # BFS(Topology sort)
        while queue:
            cur_node = queue.popleft()
            res.append(cur_node)
            for child in adj_list[cur_node]:
                in_degree[child] -= 1
                if not in_degree[child]: queue.append(child)

        return res if len(res) == numCourses else []





