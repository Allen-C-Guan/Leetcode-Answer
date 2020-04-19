import sys
from collections import defaultdict
def DFS(root, path, expend, circle, visited_set):
    # 记录当前
    path.append(root)
    if root in visited_set:
        return
    expend.append(root)
    visited_set.add(root)
    for next_node in node_next[root]:  # 对于adj list我在入口处已经保证了递归入口一定是合法的
        # 如果有环
        if next_node in path:
            path.append(next_node)
            circle.append(path[path.index(next_node):])
            path.pop()
            continue
        # 如果没有环
        DFS(next_node, path,expend,circle,visited_set)
        path.pop()

while True:
    try:
        inputs_list = sys.stdin.readline().strip("\n").split(";")
        node_next = defaultdict(list)
        # 记住head
        head = (inputs_list[0].split())[0]
        # 建立adj list
        for e in inputs_list:
            root,next = e.split()
            node_next[root].append(next)
        # DFS
        expend = []
        circle = []
        # visted_set
        visited_set = set()
        DFS(head,[],expend,circle, visited_set)
        # output
        print("EXPAND:"+" ".join(expend))
        circle_print = []
        for c in circle:
            circle_print.append(" ".join(c))
        print("CIRCLE:"+  ";".join(circle_print))
    except:break





