while True:
    try:

        inputs = input()
        max_len = 0
        for mid in range(len(inputs)):
            cnt = 1
            for extend in range(1,min(mid,len(inputs)-mid-1)+1):
                if inputs[mid-extend] == inputs[mid+extend]:
                    cnt += 2
                else: break
            max_len = max(cnt, max_len)

        for mid_left in range(len(inputs)-1):
            cnt = 0
            for extend in range(min(mid_left,len(inputs)-1-mid_left-1)+1):
                if inputs[mid_left-extend] == inputs[mid_left+1+extend]:
                    cnt += 2
                else:break
            max_len = max(cnt, max_len)
        print(max_len)
    except:break