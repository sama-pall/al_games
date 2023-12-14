# крестики-нолики

import random


def drawBoard(board):
    '''Эта функция выводит на экран игровое поле, клетки которого будут заполняться'''

    '''"board"  - это список из 10 строк, для прорисовки игрового поля (индекс 0 игнорируется)'''
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def inputPlayerLetter():
    '''Разрешение игроку ввести букву, которую он выбирает.
    Возвращает список, в котором буква игрока - первый элемент, а буква компьютера - второй'''

    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Вы выбираете Х или О? ')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    # случайный выбор игрока, который ходит первым.
    if random.randint(0, 1) == 0:
        return 'Компьютер'
    else:
        return 'Человек'


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo, le):
    '''Учитывая заполнение игрового поля и буквы игрока, эта функция возвращает True, если
    игрок выигал.
    Используется "bo" "board" "le" "letter", чтобы меньше печатать
    '''
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # по диагонали
            (bo[9] == le and bo[5] == le and bo[1] == le)  # по диагонали
            )


def getBoardCopy(board):
    # makes copy of game board and returns it
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy


def isSpaceFree(board, move):
    # returns True if move is made to a free sell
    return board[move] == ' '


def getPlayerMove(board):
    # let to player make his move
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Ваш следующий ход? (1-9)')
        move = input()
    return int(move)


def chooseRandomMoveFromList(board, moveList):
    # returns possible move taking in account made moves and list of filled sells
    # returns None, if no allowed move
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):
    """Taking in account how board is filled and letter from computer, define allowed move
    and returns it
    """
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # this is algorithm for AI "Krestiki-noliki"
    # firstly check if we will win with next move
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    # check if player will win with following move and bloke it/
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    # try to choose one of the corners, if it's free
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move is not None:
        return move

    # try to choose center if it's free
    if isSpaceFree(board, 5):
        return 5

    # make move on one side
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    # return True if sell isn't free
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
        return True


print("Игра 'Крестики-нолики'")

while True:
    # reload of game board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('' + turn + ' ходит первым.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Человек':
            # ход игрока
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print("Ура! Вы выиграли!")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Ничья!')
                    break
                else:
                    turn = 'Компьютер'

        else:
            # Computer move
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('Компьютер победил! Вы проиграли.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Ничья!')
                    break
                else:
                    turn = 'Человек'

    print('Сыграем еще раз? (да или нет)')
    if not input().lower().startswith('д'):
        break
