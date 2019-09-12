try:
    raise RuntimeError('aabbbbbaa')

except RuntimeError as aaa:
    print(aaa.args)
    print(aaa.__cause__)
    print(aaa.__class__)
    print('caught here')
