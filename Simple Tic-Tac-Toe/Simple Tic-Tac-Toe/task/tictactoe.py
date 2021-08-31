gg = False
res = True
field = list(input())
# Начнём с проверки на количество ходов:
if (field.count('X') > (field.count('O') + 1)) or (field.count('O') > (field.count('X') + 1)):
    res = 'Impossible'
    gg = True
# Восемь рядов на проверку
rows = [field[0:3], field[3:6], field[6:10]]
cols = [field[:9:3], field[1:9:3], field[2:10:3]]
diags = [[field[0], field[4], field[8]], [field[2], field[4], field[6]]]
collected = []
collected += rows
collected += cols
collected += diags  # Собрали восемь штук по три


def check_win():
    winner = ''
    count = 0
    for x in collected:
        if len(set(x)) == 1:
            if winner == '':
                winner = set(x).pop()
            elif count >= 1:
                return 'Impossible'
            count += 1
    return winner


out = '''
---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------
'''.format(*field)
print(out)

if gg:
    print(res)
if not gg:
    res = check_win()
    if res == 'Impossible':
        print(res)
    elif res == 'X' or res == 'O':
        print(res, 'wins')
    elif not res and '_' in field:
        print('Game not finished')
    else:
        print('Draw')
