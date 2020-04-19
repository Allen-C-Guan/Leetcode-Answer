first_str = input()
second_str = input()
if len(first_str)%8:
    first_str += (8-(len(first_str)%8)) * "0"
if len(second_str)%8:
    second_str += (8-(len(first_str)%8)) * "0"
for i in range(int(len(first_str)/8)):
    print(first_str[i*8:i*8+8])
for i in range(int(len(second_str)/8)):
    print(second_str[i*8:i*8+8])