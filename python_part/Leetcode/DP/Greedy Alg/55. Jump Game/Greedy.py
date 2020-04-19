'''
贪心法典型题：
该题给出的是最大跳跃距离，最大意味着每一步都可以有很多种选择，如果采用回朔或者递归或者暴力法，这将是一个指数级别的问题。
当然还可以使用dp来解决问题。 可是该题既然已经有了最大这么一个关键词，那么就用dp的亲戚，贪心法来解决这个问题。

这个问题的关键点在于理解：
        若最远可以到达k点，那么k点之前的任何一个点，均可以到达！！！

这是因为：
    最远距离一定是通过至少一个路径达到的。若最远距离是由 a, b, c 三点构成的。那么其中间的任何一点，即使无法达到终点，但是也一定可以到达该点。
    因为若可以从a到b，那么a b之间任何一个点均可以到达。这是最大跳跃的性质。同理b c之间任何一个点也可以到达。
    因此，从a到c之间的任何一个点都可以从a出发并到达。

因此我们的思路可以是： 遍历数组，并实时更新最远到达距离。
具体做法：若当前最远到达距离左边的任何一个点大于当前最远距离，则更新最远距离。
剪枝：若当前位置已经大于了最大可到达位置，说明已经出现了短路，遍历结束。

若最远到达距离大于等于终点位置，那么就是true。
'''

from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        max_dist = 0
        for index, n in enumerate(nums):
            if index > max_dist: return False
            max_dist = max(index + n, max_dist)
            if max_dist > size: break
        return True

