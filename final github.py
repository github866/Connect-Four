# made by mightyclimax
def instructions():
    '''
    Here are the following rules for playing Connect Four:
        1. Player 1 always play first
        2. Both player need to choose their color first and then play the game
        3. The game follows the exact rule of Connect Four:
        player wins the game connect 4 same color diagonally or on straight line

    '''

# if color is included in the list


def identify_color():
    color = input("choose your color: ")
    list_color = ['red', 'green', 'orange', 'purple', 'pink',
                  'yellow', 'cyan', 'gray', 'brown', 'olive', 'black']
    while True:
        try:
            if color in list_color:
                return color
                break
            else:
                color += 1
        except:
            color = input('please choose your color again: ')

# main code of choose color

def choosecolor():
    '''
    Here are some options from colors:
        red, green, orange, purple, pink,
        yellow, cyan, gray, brown, olive, black


    '''
    while True:
        try:
            print('player 1', end=' ')
            player1_color = identify_color()
            print()
            print('player 2', end=' ')
            player2_color = identify_color()
            if player1_color != player2_color:
                return [player1_color, player2_color]
                break
            else:
                player1_color = int(player1_color)
        except:
            print()
            print("Players are not allow to choose the same color, try again")
            print()
            print('player 1', end=' ')
            player1_color = identify_color()
            print()
            print('player 2', end=' ')
            player2_color = identify_color()
    return [player1_color, player2_color]

# good_piece_position, restricts via the board
def good_piece(a):
    x = input("Put your piece in one column: ")
    while True:
        try:
            x = int(x)
            if x <= 7 and x > 0 and a[x-1][1] == '':
                break
            else:
                x = x + 'i'
            
        except:
            x = input("Try Again: ")
    return x


def winning(player):
    Flag = True
    Flag1 = True
    for j in range(6):  # column
        for ding in range(0, 4):
            # digonial from left bottom to right up
            if player[ding][j] == 1 and player[ding+1][j+1] == 1 and player[ding+2][j+2] == 1 and player[ding+3][j+3] == 1:
                Flag = False
                break
        for ding in range(3, 7):
            # digonial from left up to right bottom
            if player[ding][j] == 1 and player[ding-1][j+1] == 1 and player[ding-2][j+2] == 1 and player[ding-3][j+3] == 1:
                Flag = False
                break

    for i in range(7):  # row
        for j in range(6):  # column
            if player[i][j] == 1 and player[i][j+1] == 1 and player[i][j+2] == 1 and player[i][j+3] == 1:
                Flag1 = False
                break
            if player[i][j] == 1 and player[i+1][j] == 1 and player[i+2][j] == 1 and player[i+3][j] == 1:
                Flag1 = False
                break

    if Flag == False or Flag1 == False:
        return True
    else:
        return False


def putting_piece(a, val):
    for i in range(6, -1, -1):
        if a[i] != '':
            continue
        else:
            a[i] = int(val)
            return [a]


# I do not know how to put the label in the bottom of the graph
# plotting the 7*6 grid line of the game
def main_section():

    # choosing color section

    colorlist = choosecolor()
    player1_color = colorlist[0]
    player2_color = colorlist[1]

    # this section draw the graph that are playing
    ax = plt.axes()
    ax.axis([0, 7, 0, 6])  # 0 <= x <= 8 and 0 <= y <= 7
    ax.set_facecolor("blue")  # background color
    ax.xaxis.set_visible(False)  # delete x-axis
    ax.yaxis.set_visible(False)  # delete y-axis
    for i in range(8):
        plt.plot([0, 7], [i, i], 'black')
    for i in range(9):
        plt.plot([i, i], [0, 8], 'black')
    # adding white dots to show empty space
    #ax.scatter(1-0.5,1-0.5, s=600, facecolor='white', edgecolor='k')
    for i in range(8):
        for j in range(7):
            ax.scatter(i-0.5, j-0.5, s=600, facecolor='white', edgecolor='k')
    ax.set_title(
        "1           2          3          4           5          6           7")
    plt.show()


    # this would be the entire board and the piece are placed in here
    board = [['', '', '', '', '', '', ''], ['', '', '', '', '', '', ''], ['', '', '', '', '', '', ''], [
        '', '', '', '', '', '', ''], ['', '', '', '', '', '', ''], ['', '', '', '', '', '', ''], ['', '', '', '', '', '', '']]

    player1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    player2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    blank = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # The maximum step is 6*7 = 42
    for step in range(42):
        plt.figure()
        # determine the winner or draw
        a = winning(player1)  # winning function is still not implemented
        b = winning(player2)
        if a == True:
            print('player 1 wins')
            break
        if b == True:
            print('player 2 wins')
            break
        elif step == 41 and b != True and a != True:
            print('a draw')
            break

        # place a piece on the board
        row = good_piece(board)
        templist = putting_piece(board[row - 1], step)
        
        for j in (board[row - 1]):  # plot the dots on the graph
            if j == step:  # determine if player 1 or 2 put pieces on the board
                #print(j)
                continue

        # this part change the 2d list from i to 1
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == step:
                    if step % 2 == 0:
                        player1[row][column] = 1
                    elif step % 2 == 1:
                        player2[row][column] = 1

        # blank color helps graph the white color on the plot
        for row in range(len(blank)):
            for column in range(len(blank[0])):
                if player1[row][column] == 1 or player2[row][column] == 1:
                    continue
                else:
                    blank[row][column] = 1



        #plotting the graph again by adding dots to the graph again
        # this section draw the graph that are playing
        ax = plt.axes()
        ax.axis([0, 7, 0, 6])  # 0 <= x <= 8 and 0 <= y <= 7
        ax.set_facecolor("blue")  # background color
        ax.xaxis.set_visible(False)  # delete x-axis
        ax.yaxis.set_visible(False)  # delete y-axis
        for i in range(8):
            plt.plot([0, 7], [i, i], 'black')
        for i in range(9):
            plt.plot([i, i], [0, 8], 'black')
        # adding white dots to show empty space
        #ax.scatter(1-0.5,1-0.5, s=600, facecolor='white', edgecolor='k')
        for i in range(8):
            for j in range(7):

                if blank[i][j] == 1:
                    ax.scatter(i + 0.5, 6.5 - j, s=600, facecolor='white', edgecolor='k')
                if player1[i][j] == 1:
                    ax.scatter(i + 0.5, 6.5 - j, s=600, facecolor=player1_color, edgecolor='k')
                    # plt.show()
                if player2[i][j] == 1:
                    ax.scatter(i + 0.5, 6.5 - j, s=600, facecolor=player2_color, edgecolor='k')
                    # plt.show()
        ax.set_title(
            "1           2          3          4           5          6           7")
        plt.show()
        
        
        
        
help(instructions)
help(choosecolor)
main_section()
