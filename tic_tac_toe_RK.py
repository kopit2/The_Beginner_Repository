#TIC_TAC_TOE_BY_Rk
line11 = ['1', '2', '3']
line22 = ['4', '5', '6']
line33 = ['7', '8', '9']
won = False
full_board = False
choices_taken = []
full = (list(range(1, 10)))
stop = False

#lets the user to choose a name (works)

print('LETS PLAY TIC TAC TOE\n')
player1 = input('PLAYER 1 PLEASE ENTER YOUR NAME: ').upper()
player2 = input('PLAYER 2 PLEASE ENTER YOUR NAME: ').upper()
print(player1 + ' IS PLAYING X\nAND ' + player2 + ' IS PLAYING O ')


#prints the board(works)


def show_board():
    print('')
    print(f'    {line11[0]}      |    {line11[1]}    |    {line11[2]}    ')
    print('           |         |')
    print('---------------------------------')
    print(f'    {line22[0]}      |    {line22[1]}    |    {line22[2]}    ')
    print('           |         |')
    print('---------------------------------')
    print(f'    {line33[0]}      |    {line33[1]}    |    {line33[2]}    ')
    print('           |         |')


#lets the player choose a position for their x/o(works)


def choose_position_p1():
    choice = 'not a num'
    choice_valid = False
    valid_range = range(1, 10)
    choice2 = 'not a num'
    choice_valid2 = False
    valid_range2 = ['X', 'O']
    while not choice_valid:
        choice = input(player1 + ': \nPLEASE CHOOSE WHERE DO YOU WANT TO PLACE YOUR X/O: ').upper()
        if int(choice.isdigit()):
            if int(choice) in valid_range and int(choice) not in choices_taken:
                choice_valid = True
                choices_taken.append(int(choice))
            else:
                print(f'NUMBER {choice} IS ALREADY CHANGED OR NUMBER IS NOT IN RANGE!!!')
        else:
            print('PLEASE ENTER A NUMBER!!!')

    while not choice_valid2:
        choice2 = input('DO YOU WANT TO REPLACE THIS TILE WITH X OR O?: ').upper()
        if choice2.isalpha() and choice2 in valid_range2:
            choice_valid2 = True
        else:
            print('X/O ONLY!!!')

    replace_xo(choice, choice2)
    show_board()


#same but with player 2(works)


def choose_position_p2():
    choice = 'not a num'
    choice_valid = False
    valid_range = range(1, 10)
    choice2 = 'not a mun'
    choice_valid2 = False
    valid_range2 = ['X', 'O']
    while not choice_valid:
        choice = input(player2 + ': \nPLEASE CHOOSE WHERE DO YOU WANT TO PLACE YOUR X/O: ').upper()
        if int(choice.isdigit()):
            if int(choice) in valid_range and int(choice) not in choices_taken:
                choice_valid = True
                choices_taken.append(int(choice))
            else:
                print(f'NUMBER {choice} IS ALREADY CHANGED OR NUMBER IS NOT IN RANGE!!!')
        else:
            print('PLEASE ENTER A NUMBER!!!')

    while not choice_valid2:
        choice2 = input('DO YOU WANT TO REPLACE THIS TILE WITH X OR O?: ').upper()
        if choice2.isalpha() and choice2 in valid_range2:
            choice_valid2 = True
            print(choice2)
        else:
            print('X/O ONLY!!!')
    replace_xo(choice, choice2)
    show_board()


#replace the num with x/o(works)


def replace_xo(choice, choice2):

    choosen_num = choice
    xo = choice2

    if int(choosen_num) in range(1, 4):
        line11[int(choosen_num) - 1] = xo
    elif int(choosen_num) in range(4, 7):
        line22[int(choosen_num) - 4] = xo
    elif int(choosen_num) in range(7, 10):
        line33[int(choosen_num) - 7] = xo


#defines is someone wins the game(after  3 hours works)


def won_game(player1, player2):
    global won
    if line11[0] == 'X' and line11[1] == 'X' and line11[2] == 'X':
        print(player1 + ' HAS WON THE GAME1!')
        won = True
        return won
    elif line11[0] == 'X' and line22[0] == 'X' and line33[0] == 'X':
        print(player1 + ' HAS WON THE GAME2!')
        won = True
        return won
    elif line11[2] == 'X' and line22[2] == 'X' and line33[2] == 'X':
        print(player1 + ' HAS WON THE GAME3!')
        won = True
        return won
    elif line11[1] == 'X' and line22[1] == 'X' and line33[1] == 'X':
        print(player1 + ' HAS WON THE GAME4!')
        won = True
        return won
    elif line22[0] == 'X' and line22[1] == 'X' and line22[2] == 'X':
        print(player1 + ' HAS WON THE GAME5!')
        won = True
        return won
    elif line33[0] == 'X' and line33[1] == 'X' and line33[2] == 'X':
        print(player1 + ' HAS WON THE GAME6!')
        won = True
        return won
    elif line11[0] == 'X' and line22[1] == 'X' and line33[2] == 'X':
        print(player1 + ' HAS WON THE GAME7!')
        won = True
        return won
    elif line11[2] == 'X' and line22[1] == 'X' and line33[0] == 'X':
        print(player1 + ' HAS WON THE GAME8!')
        won = True
        return won
    elif line11[0] == 'O' and line11[1] == 'O' and line11[2] == 'O':
        print(player2 + ' HAS WON THE GAME9!')
        won = True
        return won
    elif line11[0] == 'O' and line22[0] == 'O' and line33[0] == 'O':
        print(player2 + ' HAS WON THE GAME10!')
        won = True
        return won
    elif line11[2] == 'O' and line22[2] == 'O' and line33[2] == 'O':
        print(player2 + ' HAS WON THE GAME11!')
        won = True
        return won
    elif line11[1] == 'O' and line22[1] == 'O' and line33[1] == 'O':
        print(player2 + ' HAS WON THE GAME12!')
        won = True
        return won
    elif line22[0] == 'O' and line22[1] == 'O' and line22[2] == 'O':
        print(player2 + ' HAS WON THE GAME13!')
        won = True
        return won
    elif line33[0] == 'O' and line33[1] == 'O' and line33[2] == 'O':
        print(player2 + ' HAS WON THE GAME14!')
        won = True
        return won
    elif line11[0] == 'O' and line22[1] == 'O' and line33[2] == 'O':
        print(player2 + ' HAS WON THE GAME15!')
        won = True
        return won
    elif line11[2] == 'O' and line22[1] == 'O' and line33[0] == 'O':
        print(player2 + ' HAS WON THE GAME16!')
        won = True
        return won
    else:
        pass
    board_check()


#checks if the board is full
def board_check():
    global full_board
    if sorted(choices_taken) == full:
        print('DRAW!!!\nNO SPACE LEFT ON THE BOARD!')
        full_board = True
        return full_board
    else:
        full_board = False
        return full_board


#to play again
def play_again():
    global won
    global full_board
    global stop
    global line11
    global line22
    global line33
    answer = input('DO YOU WANT TO PLAY AGAIN?(Y/N): ').upper()
    if answer == 'Y':
        won = False
        full_board = False
        stop = False
        choices_taken.clear()
        line11 = ['1', '2', '3']
        line22 = ['4', '5', '6']
        line33 = ['7', '8', '9']
    else:
        stop = True


show_board()
while not stop:
    show_board()
    while not won and not full_board:
        choose_position_p1()
        won_game(player1, player2)
        if won or full_board:
            break
        choose_position_p2()
        won_game(player1, player2)
    play_again()
