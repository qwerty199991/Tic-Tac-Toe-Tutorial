field = [' ' for x in range(10)]
player = True
moves = 0
def check_turns():
    if (field.count('X') > (field.count('O') + 1)) or (field.count('O') > (field.count('X') + 1)):
        print_field()
        print('Impossible')
        exit(0)
        return True


def check_state():
    winner = ''
    count = 0
    rows = [field[0:3], field[3:6], field[6:10]]
    cols = [field[:9:3], field[1:9:3], field[2:10:3]]
    diags = [[field[0], field[4], field[8]], [field[2], field[4], field[6]]]
    collected = rows + cols + diags
    collected = [set(x) for x in collected]
    for x in collected:
        if len(x) == 1 and (' ' not in x) and (' ' not in x):
            count += 1
            if winner == '':
                winner = x.pop()
            elif count >= 1:
                winner = 'Impossible'
                return winner
    return winner


def print_field():
    out = '''
    ---------
    | {} {} {} |
    | {} {} {} |
    | {} {} {} |
    ---------
    '''.format(*field)
    print(out)


def make_a_move():
    global field
    global player
    global moves
    trans = [field[0:3], field[3:6], field[6:10]]
    if ' ' in field:
        move = input('Enter the coordinates: ').split()
    try:
        move = [int(x) for x in move]
        if (move[0] not in range(1, 4)) or (move[1] not in range(1, 4)):
            print('Coordinates should be from 1 to 3!')
            return
        if trans[move[0] - 1][move[1] - 1] == ' ' or trans[move[0] - 1][move[1] - 1] == ' ':
            if player:
                trans[move[0] - 1][move[1] - 1] = 'X'
                field = trans[0] + trans[1] + trans[2]
                player = False
                moves += 1
            else:
                trans[move[0] - 1][move[1] - 1] = 'O'
                field = trans[0] + trans[1] + trans[2]
                player = True
                moves += 1
        elif ' ' not in field:
            print('This cell is occupied! Choose another one!')
            return
        #if not check_turns():
        field = trans[0] + trans[1] + trans[2]
        #    print_field()

    except ValueError:
        print('You should enter numbers!')


def main():
    global moves

    state = check_state()
    print_field()
    if ' ' not in field or moves == 9:
        if not check_state():
            print('Draw')
            exit()
    if check_state() == 'X' or check_state() == 'O':
        print_field()
        print(state, 'wins')
        exit()
    elif not state and ' ' in field:
        make_a_move()
        main()
    if moves == 9:
        print_field()
        exit()

    exit()




main()

