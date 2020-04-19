while True:
    try:

        height = int(input())
        totol = height
        for i in range(4):
            totol += height
            height = height/2
        print(totol)
        print(height/2)
    except:break