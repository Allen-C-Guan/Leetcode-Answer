import re
dic = {"a":2,"b":2,"c":2,
       "d":3,"e":3,"f":3,
       "g":4,"h":4,"i":4,
       "j":5,"k":5,"l":5,
       "m":6,"n":6,"o":6,
       "p":7,"q":7,"r":7,"s":7,
       "t":8,"u":8,"v":8,
       "w":9,"x":9,"y":9,"z":9}
while True:
    try:
        inputs = input()
        if len(inputs)==0:break
        res = ""
        for c in inputs:
            if c in dic:
                res += str(dic[c])
            elif re.match(r"[A-Y]",c):
                res += chr(ord(c)+1+32)
            elif c == "Z":
                res += "a"
            else:
                res += c
        print(res)
    except:break
