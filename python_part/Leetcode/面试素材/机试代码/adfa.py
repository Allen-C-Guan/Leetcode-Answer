import sys
def checking_lable(name, pop, blue, rock, unkown):
    if name in pop:
        return pop
    if name in blue:
        return blue
    if name in rock:
        return rock
    return unkown

pop = {}
blue = {}
rock = {}
unkown = {}
last_label = None
last_state = None
while True:
    split_res = sys.stdin.readline().strip("\n").split(" ")
    if len(split_res) <= 1: break
    if split_res[0] == "I":
        if split_res[2] == "Pop":
            pop[split_res[1]] = 0
        elif split_res[2] == "Blue":
            blue[split_res[1]] = 0
        elif split_res[2] == "Rock":
            rock[split_res[1]] = 0
        else:
            unkown[split_res[1]] = 0
    else:
        cur_label = checking_lable(split_res[1], pop, blue, rock, unkown)
        cur_state, cur_name = split_res[0], split_res[1]
        if cur_state == "P":
            cur_label[cur_name] += 3
            if cur_label != unkown and cur_label == last_label and last_state == "P":
                for names in cur_label.keys():
                    if names != cur_name:
                        cur_label[names] += 1
        if cur_state == "B":
            cur_label[cur_name] -= 2
            if cur_label != unkown and  cur_label == last_label and last_label == "B":
                for names in cur_label.keys():
                    if names != cur_name:
                        cur_label[names] -= 1
        # update
        last_label, last_state = cur_label, cur_state

res = []
for key, val in pop.items():
    res.append((key,val))
for key, val in blue.items():
    res.append((key, val))

for key, val in rock.items():
    res.append((key, val))

for key, val in unkown.items():
    res.append((key, val))

sorted(res, key=lambda x:x[1]*1000 + ord(x[0]))

for name, val in res:
    print(name)