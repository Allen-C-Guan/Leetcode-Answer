'''
砝码这题就用优化版暴力法解题即可
'''
while True:
    try:
        categories = int(input())
        mass = list(map(int,input().split()))
        nums = list(map(int,input().split()))
        dp = {0}
        for m_index in range(len(mass)):
            temp = set()
            for n in range(1, nums[m_index] + 1):
                cur_mass = n * mass[m_index]
                for pre in dp:
                    temp.add(cur_mass + pre)
            dp.update(temp)
        print(len(dp))
    except:break

# categories = int(input())
# mass = list(map(int,input().split()))
# nums = list(map(int,input().split()))

# mass = [1,2]
# nums = [2,1]
# dp = {0}
# for m_index in range(len(mass)):
#     temp = set()
#     for n in range(1, nums[m_index]+1):
#         cur_mass = n * mass[m_index]
#         for pre in dp:
#             temp.add(cur_mass+pre)
#     dp.update(temp)
# print(len(dp))