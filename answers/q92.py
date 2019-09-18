def countChar(s : str):
    dic = {}
    for c in s:
        if dic.get(c, -1) == -1:
            dic[c] = 1
        else:
            dic[c] += 1
    print(dic)

countChar('abcdefgabc')
