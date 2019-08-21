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

def initializeBoard():
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
        print turn+" win!"
        return True
    else:
        #columns
        if ttt[0][int(y_move)] == ttt[1][int(y_move)] == ttt[2][int(y_move)]:
            print turn+"'s win!"
            return True
        else:
            if ttt[1][1] != '_':
                if ttt[0][0] == ttt[1][1] == ttt[2][2]:
                    print turn+" win!"
                    return True
                else:
                    if ttt[0][2] == ttt[1][1] == ttt[2][0]:
                        print turn+" win!"
                        return True

def player1_move():
    while True:
        global x_move
        global y_move
        global turn
        #player moves
        turn = player1
        print "select X cordinate"
        x_move = raw_input()
        print "select Y cordinate"
        y_move = raw_input()
        if cell_occupied() == False:
            print "Player moves"
            ttt[int(x_move)][int(y_move)] = player1
            show()
            break
        print "Cell already occupied, please select another cell"

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
            print "computer moves"
            ttt[int(x_move)][int(y_move)] = player2
            show()
            break

def whostarts():
    if random.randint(0,1) == 0:
        return 0
    else:
        return 1

#game starts
initializeBoard()
print "board initialized \n"
print "what do you want to be.. X or O?"
if raw_input().upper() == player_x:
    player1 = player_x
    player2 = player_o
else:
    player1 = player_o
    player2 = player_x

print "you are "+player1+"'s"
show()

if whostarts() == 0:
    while True:
        player1_move()
        if check_win(ttt, x_move, y_move) == True:
            break
        player2_move()
        if check_win(ttt, x_move, y_move) == True:
            break
else:
    while True:
        player2_move()
        if check_win(ttt, x_move, y_move) == True:
            break
        player1_move()
        if check_win(ttt, x_move, y_move) == True:
            break
