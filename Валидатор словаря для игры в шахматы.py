# pawn - пешка (p)
# knight - конь (k)
# bishop - слон (b)
# rook - ладья (r)
# queen - ферзь (q)
# king - король (i)
# W/B - б/ч

chess_board = {
    'a1': 'w_r', 'a2': 'w_p', 'a3': ' ', 'a4': ' ', 'a5': ' ', 'a6': ' ', 'a7': 'b_p', 'a8': 'b_r',
    'b1': 'w_k', 'b2': 'w_p', 'b3': ' ', 'b4': ' ', 'b5': ' ', 'b6': ' ', 'b7': 'b_p', 'b8': 'b_k',
    'c1': 'w_b', 'c2': 'w_p', 'c3': ' ', 'c4': ' ', 'c5': ' ', 'c6': ' ', 'c7': 'b_p', 'c8': 'b_b',
    'd1': 'w_q', 'd2': 'w_p', 'd3': ' ', 'd4': ' ', 'd5': ' ', 'd6': ' ', 'd7': 'b_p', 'd8': 'b_q',
    'e1': 'w_i', 'e2': 'w_p', 'e3': ' ', 'e4': ' ', 'e5': ' ', 'e6': ' ', 'e7': 'b_p', 'e8': 'b_i',
    'f1': 'w_b', 'f2': 'w_p', 'f3': ' ', 'f4': ' ', 'f5': ' ', 'f6': ' ', 'f7': 'b_p', 'f8': 'b_b',
    'g1': 'w_k', 'g2': 'w_p', 'g3': ' ', 'g4': ' ', 'g5': ' ', 'g6': ' ', 'g7': 'b_p', 'g8': 'b_k',
    'h1': 'w_r', 'h2': 'w_p', 'h3': ' ', 'h4': ' ', 'h5': ' ', 'h6': ' ', 'h7': 'b_p', 'h8': 'b_r'
}

def is_board_corrected(board_def): # Довольно хрупкий метод проверки, стоит переделать
    # Корректность доски
    board_hash = str()
    chek = 'a1a2a3a4a5a6a7a8b1b2b3b4b5b6b7b8c1c2c3c4c5c6c7c8d1d2d3d4d5d6d7d8e1e2e3e4e5e6e7e8f1f2f3f4f5f6f7f8g1g2g3g4g5g6g7g8h1h2h3h4h5h6h7h8'
    board_hash = ''.join(board_def.keys())
    if board_hash == chek:
        return True
    else:
        return False

def is_all_check(board_def): # НАПОМИНАЛКА! Переделать перебор, с помощью i.startswith('w_') "который позволяет проверить начинается ли i на ('w_')"
    # Проверка на не более 16 фигур на одну сторону(и от меня проверка на одного короля)
    all_chess = [['w_r', 'w_k', 'w_b', 'w_q', 'w_p'],['b_r', 'b_k', 'b_b', 'b_q', 'b_p']]
    white_check = 0
    white_pawn = 0
    black_check = 0
    black_pawn = 0
    white_king = 0
    black_king = 0

    for i in board_def.values():
        # Проверка на 2 короля(любых)
        if i == 'w_i':
            white_king += 1
        elif i == 'b_i':
            black_king += 1
        # Подсчет пешек обоих команд
        if i == 'w_p':
            white_pawn += 1
        elif i == 'b_p':
            black_pawn += 1
        # Проверка количества всех фигур на сторону <= 16 (с учетом пешек)
        for u in all_chess[0]:
            if i == u:
                white_check += 1
        for j in all_chess[1]:
            if i == j:
                black_check += 1
    if white_check <= 15 and black_check <= 15 and white_king == 1 and black_king == 1 and white_pawn <= 8 and black_pawn <= 8:
        return True
    else:
        return False

def is_valid_chess_board(board):
    if is_all_check(board) and is_board_corrected(board):
        return True
    else:
        return False


print(is_valid_chess_board(chess_board))