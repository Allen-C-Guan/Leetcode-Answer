'''
这道题主要利用了4个重点知识点：
1. Topology sort的性质: 拓扑排序。只有dag才可以拓扑排序。
        当出（入）队的个数等于图节点个数的时候是无环图，相反便是有环图。 因此进入过queue中的是在环中的点，最后BSF后没有访问到的是环的组成成员
        这是因为，我们只是不断的去掉没有in-degree的node，而环中的任何一个点，都不可能通过这种方式被去掉。也就没有被访问过（没出入过queue）。

2. BFS: 真正的BFS在这呢，不是通过简单的list来存储下一个level的内容（那是level-search，只使用于二叉树这种无环的结构）而是通过queue
    BFS和DFS都是适用于所有图的。

3. 拓扑排序的实现： BFS的改进版本。
    拓扑排序的实现，简单说，是 BFS + 筛选，只有既是下一个层级（BFS），又符合 入度==0（筛选）的点才有资格进入queue。

    1. 在BFS中我们决定是否加入下一个点的条件是 该点是否被访问过，在拓扑排序中，我们判定是否加入的方法是，
        该点入度是否为0。通过不断的访问 in-degree == 0 的点，并同时更新in-degree，来把所有可以通过拓扑排序来访问的点（入度曾经为0的点）都访问一遍。
        然后我们判定访问的点数是否和全部的点数相同，如果相同说明全部的点都不在环中，即全图无环，否则全图存在环。

    2. BFS的开头和DFS的开头相同，都是起到为了防止隔离产生的没遍历的部分而写的for循环。但是在sort中，我们采用的开头是所有in-degree == 0的点
        这也让被隔离的点直接就进入到queue中去了。不会被落下。

    问：这里有出现一个问题了，在1提出的不同点中，BFS中采用了判定该点是否已经访问过来确定是否将该点入队的方式避免重复，可是在拓扑排序中，却并没有这么做
    那会不会出现重复访问的情况。

    答：其实并不会，每个点都只会在in-degree被减成0的时候，才会被压入队。而in-degree == 0 时候的上一级应该对应的是所有上一级中的最后一个了，其他的上级
    的贡献就是不断的把该点in-degree一个一个的减少，直到最后一个的出现，将in-degree减成0，收下该点人头（将该点压入队）。
    因此，通过对in-degree的判定，可以让每一点，只有在访问最后一个上级的时候，才会被压入队。（即只被压入队一次）


4. adjacency list. adjacency list和adjacency matrix分别是两种存储图的形式。 具体使用哪一个取决于是稀疏图还是稠密图，
    而在本题中，我们发现，他给的结构应该是稀疏图。因此我们选用list。
    （并不是所有的图都要以类似于二叉树的方式来储存，这也是为什么这道题没有给Node之类的class 的原因）

'''

from typing import List
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not numCourses: return True

        # 建立 adj list 和 in-degree list
        adj_list = [set() for _ in range(numCourses)]
        in_degree = [0 for _ in range(numCourses)]
        for child, father in prerequisites:
            in_degree[child] += 1
            adj_list[father].add(child)
        queue = deque()
        # 将所有in-degree == 0 都压入queue中
        for i in range(numCourses):
            if not in_degree[i]:
                queue.append(i)
        cnt = 0
        # 开始BFS
        while queue:
            cur = queue.popleft() # 这里只能用deque不可以用list，因为pop(0)的复杂度是O(n),而deque.popleft()复杂度是O(1)
            cnt += 1   # 计数pop出来的情况，因为queue最终会空，pop出来的个数一定等于访问过的节点的个数
            for item in adj_list[cur]:
                in_degree[item] -= 1
                if not in_degree[item]:  # 如果子节点在当前节点去掉以后也变成了in-degree==0 的情况了，那子节点也拉进来。
                    queue.append(item)
        return cnt == numCourses  # 如果通过这种方式，访问了全部的节点说明该图一定没有环。




