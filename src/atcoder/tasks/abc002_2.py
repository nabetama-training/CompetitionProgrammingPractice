def resolve():
    s = input()
    print(s.translate(str.maketrans({'a': '', 'e': '', 'i': '', 'o': '', 'u': ''})))
