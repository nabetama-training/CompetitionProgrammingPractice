def resolve():
    a, b, c, d, e, f = map(int, input().split())
    print(abs(a * d + c * f + e * b - b * c - d * e - f * a) / 2)
