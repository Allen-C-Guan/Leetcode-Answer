'''
我需要处理输入
'''


s = input()
c = input()
t1 =  c.lower()
t2 = c.upper()
t3 = s.count(c.lower())
t4 = s.count(c.upper())

print(s.count(c.upper())+s.count(c.lower()))