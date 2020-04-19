'''
复杂度太高了
这道题不能用DFS，而要用二分图法。
其实我最开始的猜测是对的，他的size给出的是3万个的长度，这对于DFS来说就是个天文数字


'''

while True:
    try:
        size = int(input())
        arr = list(map(int, input().split()))
        # size = 4
        # arr = [2,2,4,4,6,6]
        cheet_dic = {}
        max_pair = 0
        def isPrime(num):
            if num in cheet_dic:
                return cheet_dic[num]
            for factor in range(2, int(num ** 0.5) + 1):
                if not num % factor:
                    cheet_dic[num] = False
                    return False
            cheet_dic[num] = True
            return True

        def DFS(arr, isleft, pre_number, begin, cnt):
            '''
            :param arr
            :param isleft: bool
            :param begin: int
            :param cnt: int
            :return:
            '''
            # 回朔出口
            if begin >= len(arr): # 所有配对的进行都要到头为止
                global max_pair
                max_pair = max(cnt, max_pair)
                return
            # 如果是左边，那就不管，继续往下走
            if isleft:
                for cur in range(begin,len(arr)):
                    DFS(arr, not isleft, arr[cur], cur+1, cnt)  # begin 往后走，cnt不变
            # 如果是右边
            else:
                for cur in range(begin, len(arr)):
                    if isPrime(pre_number+arr[cur]):  # 如果和之前配对了，那就继续往下找，不然的话，不用继续找了，说明没有一个可以和pre-left配对的。
                        DFS(arr, True, None, cur+1, cnt+1)

        DFS(arr,True,None,0,0)
        print(max_pair)
    except:break
