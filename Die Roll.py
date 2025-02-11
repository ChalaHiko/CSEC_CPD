yw = [int(i) for i in input().split()]
p = 0
if yw[0] == yw[-1] :
    print ("1/1")
else:
    p = 7 - max(yw)
    if 6 % p == 0:
        print(f"1/{6//p}")
    else:
        print(f"{p}/6")
