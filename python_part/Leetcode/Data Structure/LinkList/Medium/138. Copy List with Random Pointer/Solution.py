'''
这道题考验的主要是对deepcopy, privacy leak 和形参的理解 和对dict的使用。
这里的deepcopy意味着所有的节点都是我们新建的，为了能新建一摸一样的list我们需要记录所有关系。
这里我们可以采用一个dict， 一边遍历原来的list，把原来list的中的node当成key，新list当成value。
这样我们发现，新旧list通过这个dict可以完美一对一。

那么我们可以进行两次遍历：
1. 第一遍遍历，只是为了建立对应关系。
 这是因为我们需要等全部的node都已经新建好了，才能互联，不然就会把新的node连到旧的node上去

2. 第二遍遍历的时候，通过遍历原list，把新的关系建立起来。

只要可以保留一一对应的关系，就不愁没法还原！
'''
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        cur, mapping = head, {None:None}
        while cur:
            mapping[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            mapping[cur].next = mapping[cur.next]  # value是new node
                                                  # 因此左边是new_cur, 右边是new_next
            mapping[cur].random = mapping[cur.random]
            cur = cur.next
        return mapping[head]








