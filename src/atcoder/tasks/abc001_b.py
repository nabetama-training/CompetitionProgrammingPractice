def resolve() -> str:
    m = int(input())
    ret = '89'

    if m < 100:
        ret = '00'
    if 100 <= m <= 5000:
        m = m / 100
        ret = format(int(m), '0>2')
    if 6000 <= m <= 30000:
        ret = str(int(m / 1000 + 50))
    if 35000 <= m <= 70000:
        mm = m / 1000
        ret = str(int((mm - 30) / 5 + 80))
    print(ret)
