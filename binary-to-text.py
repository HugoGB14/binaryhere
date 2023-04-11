str_in = input()
strinl = str_in.split(' ')
str_out = ""
for o in strinl:
    num = 0
    v = 128
    string = o
    l = [c for c in string]
    for i in range(8):
        if l[i] == "1":
            num = num + v
        v = v//2
    str_out = str_out + chr(num)
print(str_out)