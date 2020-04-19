import re

# 任意汉字

u"([\u4e00-\u9fa5])"
re.match(u"[\u4e00-\u9fa5]", "汉字")



# parttern 字符串，一定用 r + "string"的形式， 否则有麻烦
partten_int = r"\d{3}"   # 有3个数字

# compile 建立一个可以重复利用的模版
partten = re.compile(partten_int)

# match 从左到右匹配，匹配成功返回match obj, 否则是none
print("match result")
print(partten.match("123"))   # 这里要严格的匹配准确，必须准确的按着形式从头到尾的匹配

# search只是用来从左到右查找而已，不用从头，只要匹配成功，就有返回，返回第一个匹配成功的
print("search result")
print(partten.search("fadf1234"))

# span() 上面两个函数的返回，如果成功了，都有span的attribute。span是一个tuple (start, end) 左闭右开的
# start() 返回的是一个int，是span的第一个元素的值

# findall(parttern, string)  找到所有符合条件的，并放在list中，没有重叠，从左到右，贪婪算法。
print("findall res")
print(partten.findall("123132412341234"))

# 或的匹配[]
partten_1 = r"r[ua]n"  #[ua]表示括号内任何一个都匹配成功了都行
parten_int = r"[1-9]"  # 1-9都行

# group ()
# 如果我们用括号把parttern 扩起来，那么他咋匹配的时候就会自动分组,一个括号一组
parttern_group = r"([0-9])([a-z])"
# group(0) 表示匹配的全部内容，不分组， group(1)表示第一部分，这里就是数字0-9其中一个，group(2)就是第二部分，a-z其中一个字母

# 多个匹配{}

parttern_multi = r"\d{2,8}"  # 2-8之间都行

# 限制前后没有东西可以用 ^parttern$ 表示这个parttern既要在开头也要在结尾


# 例子
print(" example ")
p = r"[WASD]\d{2};"
s = "A10;S20;W10;D30;X;A1A;B10A11;;A10;"
print(re.findall(p,s))