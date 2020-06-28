from typing import Tuple


def removeIfFound(target: str, needle: str) -> Tuple[bool, str]:
    if target.find(needle) < 0:
        return False, target
    return True, target.replace(needle, '')


def f(s: str, words: [str]) -> bool:
    if s == '':
        return True
    for word in words:
        ok, ret = removeIfFound(s, word)
        if ok:
            return f(ret, words)
    return False


def resolve():
    s = input()

    if f(s, ['eraser', 'erase', 'dreamer', 'dream']):
        print('YES')
    else:
        print('NO')
