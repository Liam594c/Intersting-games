board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' ',}

def player():
    p1 = "X"
    p2 = "O"
    print("请选择玩家的符号, 输入S跳过：")
    print("第一位玩家：")
    p1 = input()
    if p1 == 'S':
        p1 = 'X'
        return p1, p2
    print("第二位玩家:")
    p2 = input()
    if p2 == 'S':
        p2 = "O"
        return p1, p2
    return p1, p2

def printBoard():
    print(board[1] + "|" + board[2] + "|" + board[3])
    print('-+-+-')
    print(board[4] + "|" + board[5] + "|" + board[6])
    print('-+-+-')
    print(board[7] + "|" + board[8] + "|" + board[9])
    # print('-+-+-')


def isWin():
    print((board[1] == board[2] == board[3] and board[2]!=' '),
           (board[4] == board[5] == board[6] and board[5]!=' '),
           (board[7] == board[8] == board[9] and board[8]!=' '),
           (board[1] == board[4] == board[7] and board[4]!=' '),
           (board[2] == board[5] == board[8] and board[5]!=' '),
           (board[3] == board[6] == board[9] and board[6]!=' '),
           (board[1] == board[5] == board[9] and board[5]!=' '),
           (board[3] == board[5] == board[7] and board[5]!=' '))
    
    return((board[1] == board[2] == board[3] and board[2]!=' ') or 
           (board[4] == board[5] == board[6] and board[5]!=' ') or
           (board[7] == board[8] == board[9] and board[8]!=' ') or
           (board[1] == board[4] == board[7] and board[4]!=' ') or
           (board[2] == board[5] == board[8] and board[5]!=' ') or
           (board[3] == board[6] == board[9] and board[6]!=' ') or
           (board[1] == board[5] == board[9] and board[5]!=' ') or
           (board[3] == board[5] == board[7] and board[5]!=' '))



restart = True
print("欢迎来到井字棋游戏！")
while restart:
    p1, p2 = player()
    turn = p1
    for i in range(0,9):
        printBoard()
        print("轮到"+turn+'下棋')
        move = input()
        board[int(move)] = turn
        if isWin():
            print(turn+',赢了!')
            break
        if turn == p1:
            turn = p2
        else:
            turn = p1
        if i >= 9:
            print("你们真厉害，不分上下！接下来猜拳定胜负吧")
    print("++++++胜利场面++++++")
    printBoard()
    print("想再来一局吗？输入任意字符开始新的一轮，输入S退出游戏:")
    key = input()
    if key == "S":
        restart = False
        print('那么下次见！')
    else:
        board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' ',}
    


