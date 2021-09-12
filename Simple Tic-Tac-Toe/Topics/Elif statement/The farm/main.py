money = int(input())
if money < 23:
    print('None')
elif 23 <= money < 678:   
    print(money // 23, 'chicken', end='')
    if (money // 23) > 1:
        print('s')
elif 678 <= money < 1296:
    print(money // 678, 'goat', end='')
elif 1296 <= money < 3848:
    print(money // 1296, 'pig', end='')
    if (money // 1296) > 1:
        print('s')
elif 3848 <= money < 6769:
    print(money // 3848, 'cow', end='')
elif money >= 6769:
    print(money // 6769, 'sheep', end='')
