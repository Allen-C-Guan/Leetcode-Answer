# 这题复杂度太高了，n^2就跑不动了。因为python太慢了
while True:
    try:
        size = int(input())
        height = list[map(int,input().split(" "))]

        forward_list = [0] * size
        backward_list = [0] * size
        for cur in range(1, size):
            for left in range(cur - 1, -1, -1):
                if height[left] < height[cur]:
                    forward_list[cur] = max(forward_list[left] + 1, forward_list[cur])

        for cur in range(size - 1, -1, -1):
            for right in range(cur + 1, size):
                if height[cur] > height[right]:
                    backward_list[cur] = max(backward_list[right] + 1, backward_list[cur])

        res = 0
        for i in range(size):
            res = max(res, forward_list[i] + backward_list[i] + 1)

        print(size - res)
    except:break



