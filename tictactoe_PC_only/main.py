import random

#ttt = [row][column]
#ttt = [[00,01,02],
        #[10,11,12],
        #[20,21,22]]
ttt = [['_','_','_'],
        ['_','_','_'],
        ['_','_','_']]

player_x = 'X'
player_o = 'O'
player1 = ''
player2 = ''
turn = ''

x_move = 0
y_move = 0

player_x_wins = 0
player_o_wins = 0
ties = 0

def initializeBoard():
    #ttt = [row][column]
    #ttt = [[00,01,02],
            #[10,11,12],
            #[20,21,22]]

    print "X wins: ", player_x_wins
    print "O wins: ", player_o_wins
    print "ties: ", ties

    global ttt

    global player_x
    global player_o
    global player1
    global player2
    global turn

    global x_move
    global y_move

    ttt = [['_','_','_'],
            ['_','_','_'],
            ['_','_','_']]

    player_x = 'X'
    player_o = 'O'
    player1 = ''
    player2 = ''
    turn = ''

    x_move = 0
    y_move = 0


def show():
    print ttt[0]
    print ttt[1]
    print ttt[2]
    print ""

def cell_occupied():
    if ttt[int(x_move)][int(y_move)] == '_':
        return False
    else:
        return True

def check_win(ttt, x_move, y_move):
    #rows
    if ttt[int(x_move)][0] == ttt[int(x_move)][1] == ttt[int(x_move)][2]:
        print turn+"'s win!"
        return True
    else:
        #columns
        if ttt[0][int(y_move)] == ttt[1][int(y_move)] == ttt[2][int(y_move)]:
            print turn+"'s win!"
            return True
        else:
            if ttt[1][1] != '_':
                if ttt[0][0] == ttt[1][1] == ttt[2][2]:
                    print turn+"'s win!"
                    return True
                else:
                    if ttt[0][2] == ttt[1][1] == ttt[2][0]:
                        print turn+"'s win!"
                        return True

def check_tie(ttt):
    if any('_' in sublist for sublist in ttt):
        return False
    else:
        print "it's a tie!"
        return True

def player1_move():
    global turn
    #computer moves
    turn = player1
    while True:
        global x_move
        global y_move
        x_move = random.randint(0,2)
        y_move = random.randint(0,2)
        if cell_occupied() == False:
            print "computer 1 moves"
            ttt[int(x_move)][int(y_move)] = player1
            show()
            break

def player2_move():
    global turn
    #computer moves
    turn = player2
    while True:
        global x_move
        global y_move
        x_move = random.randint(0,2)
        y_move = random.randint(0,2)
        if cell_occupied() == False:
            print "computer 2 moves"
            ttt[int(x_move)][int(y_move)] = player2
            show()
            break

def whostarts():
    if random.randint(0,1) == 0:
        return 0
    else:
        return 1

for x in range(0, 999999):
    #game starts
    initializeBoard()
    print "board initialized \n"

    player1 = player_x
    player2 = player_o

    show()

    if whostarts() == 0:
        while True:
            player1_move()
            if check_win(ttt, x_move, y_move) == True:
                player_x_wins = player_x_wins + 1
                break
            if check_tie(ttt) == True:
                ties = ties + 1
                break
            player2_move()
            if check_win(ttt, x_move, y_move) == True:
                player_o_wins = player_o_wins + 1
                break
            if check_tie(ttt) == True:
                ties = ties + 1
                break
    else:
        while True:
            player2_move()
            if check_win(ttt, x_move, y_move) == True:
                player_o_wins = player_o_wins + 1
                break
            if check_tie(ttt) == True:
                ties = ties + 1
                break
            player1_move()
            if check_win(ttt, x_move, y_move) == True:
                player_x_wins = player_x_wins + 1
                break
            if check_tie(ttt) == True:
                ties = ties + 1
                break
