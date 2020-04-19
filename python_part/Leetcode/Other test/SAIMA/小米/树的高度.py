import sys
## sys.stdin.readline().strip()的作用和input是一样的， strip()是为了去掉后面的回车，如果没有带着strip就会有个回车。
while True:
    try:
        size = int(sys.stdin.readline().strip())
        height = 1
        child_dic = {}  # child: father
        father_dic = {str(_):[]for _ in range(size)}  # father:[child1,child2]


        for i in range(size-1):
            father, child = sys.stdin.readline().strip().split()  # child and father both str
            father_dic[father].append(child)
            child_dic[child] = father

        head = None
        for father in father_dic.keys():
            if father not in child_dic:
                head = father
                break
        # BFS
        cur_list = [head]
        height = 0
        while cur_list:
            next_list = []
            for cur in cur_list:
                next_list.extend(father_dic[cur])

            cur_list = next_list
            height += 1
        print(height)
    except:break