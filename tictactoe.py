#make empty board
board = [" "for i in range(9)]



def printboard():
    r1 = " |{}|{}|{}| ".format(board[0], board[1], board[2])
    r2 = " |{}|{}|{}| ".format(board[3], board[4], board[5])
    r3 = " |{}|{}|{}| ".format(board[6], board[7], board[8])

    print()
    print(r1)

    print(r2)

    print(r3)


#selct and play with palyr
def playermove(icon):
    if icon =='x':
        number=1
    elif icon=='o':
        number=2

    print("player number {} 's turn".format(icon))
    choice = int(input("enter your move(1-9)").strip())
    if board[choice-1] == ' ':
        board[choice - 1] = icon
    else:
        print("taken spot")
        playermove(icon)#if spot is taken mplay with that player again

#to decide vitory or draw
def victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
        (board[6] == icon and board[7] == icon and board[8] == icon) or \
        (board[0] == icon and board[3] == icon and board[6] == icon) or \
        (board[1] == icon and board[4] == icon and board[7] == icon) or \
        (board[2] == icon and board[5] == icon and board[8] == icon) or \
        (board[0] == icon and board[4] == icon and board[8] == icon) or \
        (board[2] == icon and board[4] == icon and board[6] == icon):

                return  True
    else:
            return False
def draw():
    if " " not in board:
        return True
    else:
        return False


#main loop for playing game
while True:
    printboard()
    playermove("x")
    printboard()
    if victory("x"):
        print("x wins")
        break
    elif draw():
        print("its draw..")
        break
    playermove("o")
    if victory("x"):
        printboard()
        print("x wins")
        break

    elif draw():
        print("its draw..")
        break

 