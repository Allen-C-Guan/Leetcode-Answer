import sys

def findAllPath(maze, x, y, path, res):
    def findDirection(x,y):
        if -1< x < x_size  and  -1< y < y_size and not maze[x][y] and (x,y) not in path:
            findAllPath(maze, x, y,path,res)
            path.pop()
    # 记录足迹
    path.append((x,y))
    # 当前path是一条可行路径，走到头了
    if x == x_size-1 and y == y_size-1:
        res.append(path.copy())
        return
    # 继续往下走
    findDirection(x-1,y)
    findDirection(x+1,y)
    findDirection(x,y-1)
    findDirection(x,y+1)

        # main
while True:
    try:
        inputs = sys.stdin.readline().strip("\n")
        x_size, y_size = map(int,inputs.split())
        maze = [ [] for _ in range(x_size)]
        # create maze array
        for i in range(x_size):
            maze[i] = list(map(int, sys.stdin.readline().strip("\n").split()))

        # find all path
        res = []
        findAllPath(maze,0,0,[],res)
        shortest_path_len, shortest_path = float("inf"), []
        for candidiate in res:
            if len(candidiate) < shortest_path_len:
                shortest_path_len = len(candidiate)
                shortest_path = candidiate

        # print
        for x,y in shortest_path:
            print("("+ str(x)+","+str(y)+")")
    except:break



