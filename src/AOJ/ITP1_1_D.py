def resolve():
    s = int(input())
    hh = int(s / (60 * 60))
    mm = int(s % 3600 / 60)
    ss = int(s % 3600 % 60)
    print("{:02d}:{:02d}:{:02d}".format(hh, mm, ss))
