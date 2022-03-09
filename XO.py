def new_game():
    return [['-' for j in (1, 2, 3)] for i in (1, 2, 3)]

# функция для отображение игрового поля
def print_game_pole(game_pole):
    count = 0
    print(' ', *[1, 2, 3])
    for line in game_pole:
        count += 1
        print(count, *line, end='\n')

# функция для проверки победы
def win(game_pole, sign):
    for i in (0, 1, 2):
        if ''.join([x for x in game_pole[i]]).count(sign) == 3:
            print(sign, 'win')
            return 1
        if ''.join([x[i] for x in game_pole]).count(sign) == 3:
            print(sign, 'win')
            return 1
    if ''.join([game_pole[i][i] for i in (0, 1, 2)]).count(sign) == 3:
        print(sign, 'win')
        return 1
    if ''.join([game_pole[i][len(game_pole) - 1 - i] for i in (0, 1, 2)]).count(sign) == 3:
        print(sign, 'win')
        return 1

# функция хода игрока, проверка ввода на валидность
def make_move():
    while True:
        print('Make your move. X or O:')
        print('X coordinate:1,2,3')
        x = int(input().split()[:1][0])
        print('Y coordinate:1,2,3')
        y = int(input().split()[:1][0])
        move = (x - 1, y - 1)

        if x in (1, 2, 3) and y in (1, 2, 3) and is_available(move):
            break
        else:
            print('Non correct input')

    return move

#проверка валидности клетки игрового поля
def is_available(move):
    if str(game_pole[move[1]][move[0]]) == '-':
        return True
    else:
        return False

#изменение игрового поля при ходе игрока/cpu
def append_move(move, sign):
    game_pole[move[1]][move[0]] = sign

# алгорит действия для реакции cpu на ходы игрока
def check_line(game_pole, move_list, sign):
    if len(move_list) == 0:

        if game_pole[1][1] == '-':
            move = (1, 1)
            move_list.append(move)
            return move
        else:
            for move in ((0, 0), (0, 2), (2, 2), (2, 0)):
                if is_available(move):
                    move_list.append(move)
                    return move
    else:

        if [game_pole[i][i] for i in (0, 1, 2)].count(sign) == 2 \
                and [game_pole[i][i] for i in (0, 1, 2)].count('-') == 1:

            pos = [game_pole[i][i] for i in (0, 1, 2)].index('-')
            move = (pos, pos)
            move_list.append(move)
            return move
        if [game_pole[i][len(game_pole) - i - 1] for i in (0, 1, 2)].count(sign) == 2 \
                and [game_pole[i][len(game_pole) - i - 1] for i in (0, 1, 2)].count('-') == 1:

            pos = [game_pole[i][len(game_pole) - i - 1] for i in (0, 1, 2)].index('-')
            move = (len(game_pole) - pos - 1, pos)
            move_list.append(move)
            return move
        for i in (0, 1, 2):
            if [x for x in game_pole[i]].count(sign) == 2 \
                    and [x for x in game_pole[i]].count('-') == 1:

                pos = [x for x in game_pole[i]].index('-')
                move = (pos, i)
                move_list.append(move)
                print(move)
                return move
            if [x[i] for x in game_pole].count(sign) == 2 \
                    and [x[i] for x in game_pole].count('-') == 1:

                pos = [x[i] for x in game_pole].index('-')
                move = (i, pos)
                move_list.append(move)
                return move
        move_list_r = move_list.copy()
        move_list_r.reverse()
        for m in move_list_r:
            if [game_pole[i][i] for i in (0, 1, 2)].count(sign) == 1 \
                    and [game_pole[i][i] for i in (0, 1, 2)].count('-') == 2:

                pos = [game_pole[i][i] for i in (0, 1, 2)].index('-')
                move = (pos, pos)
                move_list.append(move)
                return move

            if [game_pole[i][len(game_pole) - i - 1] for i in (0, 1, 2)].count(sign) == 1 \
                    and [game_pole[i][len(game_pole) - i - 1] for i in (0, 1, 2)].count('-') == 2:

                pos = [game_pole[i][len(game_pole) - i - 1] for i in (0, 1, 2)].index('-')
                move = (len(game_pole) - pos - 1, pos)
                move_list.append(move)
                return move
            if [x for x in game_pole[m[1]]].count(sign) == 1 \
                    and [x for x in game_pole[m[1]]].count('-') == 2:

                pos = [x for x in game_pole[m[1]]].index('-')
                move = (pos, m[1])
                move_list.append(move)
                return move
            if [x[m[0]] for x in game_pole].count(sign) == 1 \
                    and [x[m[0]] for x in game_pole].count('-') == 2:

                pos = [x[m[0]] for x in game_pole].index('-')
                move = (m[0], pos)
                move_list.append(move)
                return move

# проверка на возможность выигрыша для CPU
def may_win(game_pole, sign):
    if [game_pole[i][i] for i in (0, 1, 2)].count(sign) == 2 \
            and [game_pole[i][i] for i in (0, 1, 2)].count('-') == 1:
        return 1
    if [game_pole[i][len(game_pole) - i - 1] for i in (0, 1, 2)].count(sign) == 2 \
            and [game_pole[i][len(game_pole) - i - 1] for i in (0, 1, 2)].count('-') == 1:
        return 1
    for i in (0, 1, 2):
        if [x for x in game_pole[i]].count(sign) == 2 \
                and [x for x in game_pole[i]].count('-') == 1:
            return 1
        if [x[i] for x in game_pole].count(sign) == 2 \
                and [x[i] for x in game_pole].count('-') == 1:
            return 1

# проверка наличия ходов для игрока/cpu
def no_more(game_pole):
    if 'o' in [game_pole[i][i] for i in (0, 1, 2)] \
            and 'x' in [game_pole[i][i] for i in (0, 1, 2)]:
        flag = False
    else:
        flag = True
    if 'o' in [game_pole[i][len(game_pole) - i - 1] for i in (0, 1, 2)] \
            and 'x' in [game_pole[i][len(game_pole) - i - 1] for i in (0, 1, 2)]:
        flag = False
    else:
        flag = True
    for i in (0, 1, 2):
        if 'o' in [x for x in game_pole[i]] \
                and 'x' in [x for x in game_pole[i]]:
            flag = False
        else:
            flag = True
        if 'o' in [x[i] for x in game_pole] \
                and 'x' in [x[i] for x in game_pole]:
            flag = False
        else:
            flag = True

    return flag


game_pole = new_game()
print_game_pole(game_pole)
move_list = []

while 1:
    X_move = make_move()
    O_move = None
    append_move(X_move, 'x')
    print_game_pole(game_pole)
    if win(game_pole, 'x'):
        break
    if (sum(game_pole, [])).count('-') == 0 or not no_more(game_pole):
        print('it\'s all')
        break
    O_move = check_line(game_pole, move_list, 'o')
    if not may_win(game_pole, 'o'):
        O_move = check_line(game_pole, move_list, 'x')

    append_move(O_move, 'o')
    print_game_pole(game_pole)
    if win(game_pole, 'o'):
        break
    if (sum(game_pole, [])).count('-') == 0:
        print('it\'s all')
        break
print('game over')
