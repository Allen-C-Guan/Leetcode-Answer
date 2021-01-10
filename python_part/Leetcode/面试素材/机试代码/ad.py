import sys

inputs = sys.stdin.readline().strip("\n")
whole_set = list(inputs)
high_rank = {"b", "d", "f", "h", "k", "l"}
mid_rank = set("aceimnorstuvwxz")
low_rank = set("gjpqy")

high_res = []
mid_res = []
low_res = []
for s in whole_set:
    if s in high_rank: high_res.append(s)
    elif s in mid_rank: mid_res.append(s)
    elif s in low_rank: low_res.append(s)
if high_res: print("".join(sorted(high_res)))
else: print("null")
if mid_res:print("".join(sorted(mid_res)))
else: print("null")
if low_res: print("".join(sorted(low_res)))
else: print("null")