import re
while True:
    try:
        move_list = input().split(";")
        x = y = 0
        for move in move_list:
            if not re.match(r"^[WASD]\d{1,2}$", move): continue
            direction, dist = move[0], int(move[1:])
            if direction == "W": y += dist
            if direction == "S": y -= dist
            if direction == "A": x -= dist
            if direction == "D": x += dist
        print(str(x) + "," + str(y))
    except:
        break



