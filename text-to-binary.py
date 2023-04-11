str_in = input()
l = []
v = 128
str_out = ""
stra = ""

for i in str_in:
    l.append(i)
for e in l:
    stra = ""
    v = 128
    word = ord(e)
    for o in range(8):
        if word >= v:
            stra = stra + "1"
            word = word - v
        else:
            stra = stra + "0"
        v = v//2
    str_out = str_out + f"{stra} "
print(str_out)