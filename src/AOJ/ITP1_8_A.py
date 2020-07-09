def resolve():
    s = input()

    ret = ""
    for c in s:
        ret += c.swapcase() # lower() <-> upper()
    print(ret)
