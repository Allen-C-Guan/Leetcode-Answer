import sys
from collections import defaultdict
def DFS(root, tracking, EXPEND, CIRCLE, duplicated_set):
    # 记录当前
    tracking.append(root)
    if root in duplicated_set:
        return
    EXPEND.append(root)
    duplicated_set.add(root)
    for next_node in next_dic[root]:
        if next_node in tracking:
            tracking.append(next_node)
            CIRCLE.append(tracking[tracking.index(next_node):])
            tracking.pop()
            continue
        # 如果没有环
        DFS(next_node, tracking, EXPEND, CIRCLE, duplicated_set)
        tracking.pop()

while True:
    try:
        # oj
        inputs_list = sys.stdin.readline().strip("\n").split(";")
        next_dic = defaultdict(list)
        first_node = (inputs_list[0].split())[0]

        for e in inputs_list:
            root,next = e.split()
            next_dic[root].append(next)

        # begin DFS
        EXPEND = []
        CIRCLE = []
        duplicated_set = set()
        DFS(first_node, [], EXPEND, CIRCLE, duplicated_set)
        # output
        print("EXPAND:" + " ".join(EXPEND))

        for i in range(len(CIRCLE)):
            CIRCLE[i] = " ".join(CIRCLE[i])
        print("CIRCLE:" +  ";".join(CIRCLE))
    except:break





