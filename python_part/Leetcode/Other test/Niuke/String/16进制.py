'''
在python中，所有非10进制都用字符串表示，而转化成十进制都方法就是 int(str, 进制：int）
'''
while True:
    try:
        h = input()
        print(int(h,16))
    except:
        break