from typing import List
'''
每次一个 + 最少几个，这完全就是为BFS而设计的

这个方法没有丝毫剪枝的BFS说实话有点复杂

'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def isNeighbour(cur:str, next:str):
            cnt = 0
            for i in range(len(cur)):
                cnt += int(cur[i]!=next[i])
            # if cnt == 1:dic[next] = False
            return cnt == 1

        dic = {}
        for _ in wordList:
            dic[_] = True

        step, cur_level = 1, [beginWord]
        while cur_level:
            next_level = []
            step += 1
            for cur in cur_level:
                for next_word, notDuplicate in dic.items():
                    if notDuplicate and isNeighbour(cur, next_word):   # 这里复杂度就高了，每次都要筛查所有元素，来选出没选过的邻居
                        if next_word == endWord: return step
                        next_level.append(next_word)
                        dic[next_word] = False
            cur_level = next_level
        return 0

foo = Solution()
print(foo.ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]))






