from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        def pickUp(begin:int):  # 选取当前行可用的所有words
            cur_len, cur_index = 0, begin
            while cur_len <= maxWidth and cur_index < len(words):    # 一直选到超过最大宽度为止 or 超过word为止
                t1 = words[cur_index]
                cur_len += len(words[cur_index])+1 # +1表示空格
                cur_index += 1
            cur_index -= 1  # 最后一定会多一个

            if cur_len <= maxWidth: # 最后一行了。
                return cur_index+1, True

            if cur_len-1 == maxWidth: # 如果只是大一个字符，那是因为最后一个多余的空格，去掉就行了
                cur_index += 1

            return cur_index, False
        def arrangement(cur_begin:int, cur_end:int):
            word_sum_len = 0
            for word in words[cur_begin:cur_end]:
                word_sum_len += len(word)
            # 中间的gap有多少个（植树问题）
            gap = cur_end - cur_begin - 1

            # gap等于0的情况没有考虑
            if gap == 0:
                return words[cur_begin] + (maxWidth-len(words[cur_begin]))*" "

            # 当gap不为0的时候， 分配gap
            average_gap = int((maxWidth - word_sum_len) / gap)
            # 除了最后一个都要被分配gap
            cur_line = []
            for word in words[cur_begin:cur_end - 1]:
                cur_line.append(word + average_gap * " ")
            # 分配剩下的space给前面的
            for i in range((maxWidth - word_sum_len) % gap):
                cur_line[i] += " "
            return "".join(cur_line) + words[cur_end - 1]


        cur_begin, res = 0, []
        while cur_begin < len(words):
            cur_end, isLast = pickUp(cur_begin)  # 第cur_end 是不应该被包括在当前行的
            # 如果是最后一行，
            if isLast:
                last_line = ""
                for word in words[cur_begin:cur_end]:
                    last_line += word + " "
                last_line = last_line.strip()
                last_line += (maxWidth - len(last_line)) * " "  # 补上缺的空格
                res.append(last_line)
            # 如果不是最后一行
            else:
                res.append(arrangement(cur_begin, cur_end))
            cur_begin = cur_end
        return res



foo = Solution()
res = (foo.fullJustify(["What","must","be","acknowledgment","shall","be"],16))
print(res)
for r in res:
    print(r)

for r in res:
    print(len(r))