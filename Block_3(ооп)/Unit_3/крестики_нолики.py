# Объявить класс.
class Board:

    def make_board(self, row, col):
        self.board = [[" " for _ in range(row)] for _ in range(col)]
        return self.board

    # Метод, который обрабатывает ходы игроков.
    def make_move(self, row, col, player):
        self.board[row][col] = player
        return self.board

    # Метод, который отрисовывает игровое поле.
    def display(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def diagonal_winner(self, board, player):
        ind = 0
        a = True
        if a:
            for item in board:
                for ind in range(len(board[0])):
                    if item[ind] == player:
                        a = True
                        ind += 1
                        break
                    else:
                        a = False

        if a:
            return True
        else:
            ind = 0
            a = True
            if a:
                for item in board:
                    for ind in range(len(board[0]) - 1, -1, -1):
                        if item[ind] == player:
                            a = True
                            ind += 1
                            break
                        else:
                            a = False

            if a:
                return True
            else:
                return False

    def row_winner(self, board, player):
        for item in range(len(board)):
            k = 0
            for x in board[item]:
                if x == player:
                    k += 1
                if k == len(board[0]):
                    return True
        return False

    def col_winner(self, board, player):
        for i in range(len(board[0])):
            k = 0
            for item in board:
                if item[i] == player:
                    k += 1
                if k == len(board):
                    return True
        return False

    def check_winner(self, board, player):
        if (
            (self.diagonal_winner(board, player))
            or (self.row_winner(board, player))
            or (self.col_winner(board, player))
        ):
            print(f"Победил игрок, игравший за {player}")
            return False
        elif all([x == " " for x in board[i]] for i in range(len(board))):
            print("Игра продолжается")
            return True
        else:
            print("Ничья!")
            return False


print(
    """
                            Приветствуем в игре крестики нолики!
Выберите размерность поля (для крестиков-ноликов число строк и столбцов должно быть равно!)
                               Первым ходит игрок с крестиками
    """
)
a, b = map(int, input("Введите размерность: ").split())

game = Board()
board = game.make_board(a, b)
game.display()
iteration = True
player_1 = "X"
player_2 = "O"
player_ = player_1
while iteration:
    a1, b1 = map(int, input("Введите клетку: ").split())
    if board[a1-1][b1-1]==' ':
        board = game.make_move(a1 - 1, b1 - 1, player_)
        game.display()
        iteration = game.check_winner(board, player_)
        player_1, player_2 = player_2, player_1
        player_ = player_1
    else:
        print('Эта клетка уже занята, выбери другую')