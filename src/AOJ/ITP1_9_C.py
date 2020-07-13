def resolve():
    n = int(input())

    score_t = 0
    score_h = 0
    for _ in range(n):
        t, h = map(str, input().split())
        if t == h:
            score_t += 1
            score_h += 1
        if t > h:
            score_t += 3
        if h > t:
            score_h += 3
    print(score_t, score_h)
