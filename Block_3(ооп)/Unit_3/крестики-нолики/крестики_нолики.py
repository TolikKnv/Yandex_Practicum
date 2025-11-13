from parts import Board


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
    if board[a1 - 1][b1 - 1] == " ":
        board = game.make_move(a1 - 1, b1 - 1, player_)
        game.display()
        iteration = game.check_winner(board, player_)
        player_1, player_2 = player_2, player_1
        player_ = player_1
    else:
        print("Эта клетка уже занята, выбери другую")
