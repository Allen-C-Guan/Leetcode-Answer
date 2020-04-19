'''
牛逼！！ 你在原来基础上覆盖着写，这样只有后面写的长度超过上一个最长stack的时候，才会影响上一个subset，同时也保证了上一个subset。 这是这样会让复杂度变成O(n^2)
'''


def lengthOfLIS(nums) -> int:
    stack, maxlength, pre_max = [], 0, float("-inf")
    for item in nums:
        ########修改部分########
        if stack and stack[-1] >= item:
            for j in range(len(stack)):
                if stack[j] >= item:
                    stack[j] = item
                    break
        else:
            stack.append(item)
        #######################
        if len(stack) > maxlength:
            maxlength, pre_max = len(stack), item
        elif item > pre_max:
            maxlength, pre_max = maxlength+1, item
    return maxlength


print(lengthOfLIS([11,12,13,14,15,16,1,2,3,4,1,5,6,7,1,8]))