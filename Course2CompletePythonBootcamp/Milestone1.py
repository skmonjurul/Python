# from IPython.display import clear_output

#display board
def display_board(board):
    # clear_output()  # Remember, this only works in jupyter!
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
test_board=['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)

#choose marker
def choose_marker():
    marker=''
    while not(marker=='X' or marker == 'O'):
        marker=input('what is your choice: X or O: ').upper()
    
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')
#choose_marker()

#assign values to board:
def assign_values(board,pos,marker):
    board[pos]=marker

#check win
def win_check(board):
    return 
    ((board[7]==board[8]==board[9]) or
    (board[4]==board[5]==board[6]) or
    (board[1]==board[2]==board[3]) or
    (board[1]==board[4]==board[7]) or
    (board[2]==board[5]==board[8]) or
    (board[3]==board[6]==board[9]) or
    (board[3]==board[5]==board[7]) or
    (board[1]==board[5]==board[9]))
# win_check(test_board)

#check empty position
def check_space(board,pos):
        return board[pos]==''

#check_space(test_board,8)

#check empty board
def check_board_space(board):
    for i in range(1,10):
        if check_space(board,i):
            return False
    return True

#enter player values
def player_choice(board):
    pos=0
    while(pos not in [1,2,3,4,5,6,7,8,9] or not check_space(board,pos)):
        pos=int(input('Enter the position from 1 to 9: '))
        print('after input')
    return pos

def replay():
    rep=input('do u wanna replay, yes or no: ').lower()[0]
    return rep=='y'

#player_choice(test_board)

print('Welcome to the game')
the_board=['']*10
val=0
while(True):
    display_board(the_board)
    player1_marker,player2_marker=choose_marker()
    while(True):
        display_board(the_board)
        position=player_choice(the_board)
        assign_values(the_board,position,player1_marker)
        val+=1
        print('after assigning '+str(val)+' value ')
        if(win_check(the_board)):
            display_board(the_board)
            print('win')
            break
        else:
            if(check_board_space(the_board)):
                print('game is draw')
                break
            else:
                continue
    if not replay():
        break