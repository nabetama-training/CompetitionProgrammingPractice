from decimal import Decimal, ROUND_HALF_UP


def get_dir(deg: int) -> str:
    if deg <= 0:
        return 'C'
    if deg < 11.25:
        return 'N'
    if deg < 33.75:
        return 'NNE'
    if deg < 56.25:
        return 'NE'
    if deg < 78.75:
        return 'ENE'
    if deg < 101.25:
        return 'E'
    if deg < 123.75:
        return 'ESE'
    if deg < 146.25:
        return 'SE'
    if deg < 168.75:
        return 'SSE'
    if deg < 191.25:
        return 'S'
    if deg < 213.75:
        return 'SSW'
    if deg < 236.25:
        return 'SW'
    if deg < 258.75:
        return 'WSW'
    if deg < 281.25:
        return 'W'
    if deg < 303.75:
        return 'WNW'
    if deg < 326.25:
        return 'NW'
    if deg < 326.25:
        return 'NW'
    if deg < 348.75:
        return 'NNW'
    return 'N'


def get_wind(w: float) -> int:
    if w <= 0.2:
        return 0
    if w <= 1.5:
        return 1
    if w <= 3.3:
        return 2
    if w <= 5.4:
        return 3
    if w <= 7.9:
        return 4
    if w <= 10.7:
        return 5
    if w <= 13.8:
        return 6
    if w <= 17.1:
        return 7
    if w <= 20.7:
        return 8
    if w <= 24.4:
        return 9
    if w <= 28.4:
        return 10
    if w <= 32.6:
        return 11
    return 12


def resolve():
    deg, dis = map(int, input().split())
    dir = get_dir(deg / 10)

    wind = Decimal(str(dis / 60)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
    w = get_wind(float(wind))

    if w == 0:
        dir = 'C'

    print("{} {}".format(dir, w))
