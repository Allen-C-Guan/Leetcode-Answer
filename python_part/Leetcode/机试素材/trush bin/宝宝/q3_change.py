import sys
from collections import defaultdict
def DFS(root, tracking):
    tracking.append(root)
    # 记录当前
    if root in duplicated_set:
        return
    EXPEND.append(root)
    duplicated_set.add(root)
    for next_node in next_dic[root]:
        # if there not circle
        if next_node not in tracking:
            DFS(next_node, tracking)
            tracking.pop()
        # if there is circle
        else:
            tracking.append(next_node)
            CIRCLE.append(tracking[tracking.index(next_node):])
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
        DFS(first_node, [])
        # output
        EXPEND = "EXPAND:" + " ".join(EXPEND)
        print(EXPEND)
        for i in range(len(CIRCLE)):
            CIRCLE[i] = " ".join(CIRCLE[i])
        print("CIRCLE:" +  ";".join(CIRCLE))
    except:break





