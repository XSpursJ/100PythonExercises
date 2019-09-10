while True:
    s = input("Yes or no?:")
    if s:
        if s.lower().strip() == 'yes':
            print('YES!!!')
        else:
            print('NO!')
    else:
        break
