
board = ((['_'] ,['_'] ,['_']) ,(['_'] ,['_'] ,['_']) ,(['_'] ,['_'] ,['_']))

def print_board():
    print(' ', '1' ,' ', '2' ,' ', '3')
    print('A ', *board[0][0], '|', *board[0][1], '|', *board[0][2])
    print('B ', *board[1][0], '|', *board[1][1], '|', *board[1][2])
    print('C ', *board[2][0], '|', *board[2][1], '|', *board[2][2])
    return

class Player():

    def __init__(self, name=str, symbol=str):
        self.name=name
        self.symbol=symbol

    def get_valid_input(self):
        move = input(f'{self.name.title()}, enter coordinate of desired move:  ')
        while not len(move) == 2:
            print(
                "Move must be a 2-digit coordinate corresponding to a location on the board in your terminal. Example: '1a'")
            move = input(f'{self.name.title()}, enter coordinate of desired move:  ')
        while move[0] not in ['1', '2', '3'] and move[1] not in ['1', '2', '3']:
            print('Move must contain a row reference and a column reference. Column reference is missing.')
            move = input(f'{self.name.title()}, enter coordinate of desired move:  ')
        while move[0].lower() not in ['a', 'b', 'c'] and move[1].lower() not in ['a', 'b', 'c']:
            print('Move must contain a row reference and a column reference. Row reference is missing.')
            move = input(f'{self.name.title()}, enter coordinate of desired move:  ')

        for char in move:
            if char.isalpha():
                if char.lower() == 'a':
                    row = 0
                if char.lower() == 'b':
                    row = 1
                if char.lower() == 'c':
                    row = 2
            if char.isnumeric():
                if 3 >= int(char) >= 1:
                    col = int(char) - 1

        return row, col

    def play_move(self):
        row, col = self.get_valid_input()
        if board[row][col][0] == '_':
            board[row][col][0] = self.symbol
        else:
            print('Position already occupied. Try another move.')
            return self.play_move()

def check_filled_spaces():
    filled_spaces = 0
    for i in range(3):
        for j in range(3):
            if board[i][j][0] != '_':
                filled_spaces += 1
    return filled_spaces

def check_for_win():
    win = False
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2] and board[i][0][0]!='_':
            win = True
            return win
        if board[0][i]==board[1][i]==board[2][i] and board[0][i][0]!='_':
            win = True
            return win
        if board[0][0]==board[1][1]==board[2][2] and board[0][0][0]!='_':
            win = True
            return win
        if board[2][0] == board[1][1] == board[0][2] and board[2][0][0]!='_':
            win = True
            return win
    return win



if __name__ == '__main__':
    p1_name = input("Player 1, please type your name:  ")
    p2_name = input("Player 2, please type your name:  ")

    player1 = Player(name=p1_name, symbol="X")
    player2 = Player(name=p2_name, symbol='O')

    turn = 0
    win_status = False

    while not win_status:
        if check_filled_spaces() < 9:
            turn += 1
            print(f"Turn {turn}:")
            print_board()
            if turn % 2 != 0:
                player1.play_move()
            else:
                player2.play_move()

        else:
            print_board()
            print("Tie Game!")
            break
        win_status = check_for_win()
        if win_status:
            if turn % 2 != 0:
                print_board()
                print(f"{player1.name} wins! Game over.")
            else:
                print_board()
                print(f"{player2.name} wins! Game over.")
