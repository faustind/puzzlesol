# In Oboedencia Veritas

# UVa 10196


import collections

Piece = collections.namedtuple('Piece', ['rank', 'row', 'col'])
def on_board(pos):
    """Return True if pos is on the board"""
    return ((0 <= pos[0] <= 7) and (0 <= pos[1] <= 7))

def capture_moves(piece, king):
    """Does the piece capture the king ?"""
    if piece.rank == 'p':
        return (king.row, king.col) in { pos for pos in [
                                 (piece.row+1, piece.col-1),
                                 (piece.row+1, piece.col+1)]
                if on_board(pos) }

    if piece.rank == 'P':
        return (king.row, king.col) in { pos for pos in [
                                 (piece.row-1, piece.col-1),
                                 (piece.row-1, piece.col+1)]
                if on_board(pos) }

    if piece.rank in ('n', 'N'):
        return (king.row, king.col) in { pos for pos in [
                                 (piece.row-2, piece.col-1),(piece.row-2, piece.col+1),
                                 (piece.row-1, piece.col-2), (piece.row-1, piece.col+2),
                                 (piece.row+1, piece.col-2), (piece.row+1, piece.col+2),
                                 (piece.row+2, piece.col-1), (piece.row+2, piece.col+1)]
                if on_board(pos) }

    if piece.rank in ('b', 'B', 'Q', 'q'):
        diag45 = piece.row + piece.col
        diag135 = piece.row - piece.col
        if king.row + king.col == diag45:
            below, above = (piece, king) if piece.row > king.row else (king, piece)
            for (r, c) in zip(range(above.row+1, below.row),
                              range(above.col-1, below.col, -1)):
                if board[r][c] != '.':
                    return False
            return True

        if king.row - king.col == diag135:
            below, above = (piece, king) if piece.row > king.row else (king, piece)
            for (r, c) in zip(range(above.row+1, below.row),
                              range(above.col+1, below.col)):
                if board[r][c] != '.':
                    return False
            return True

    if piece.rank in ('r', 'R', 'Q', 'q'):
        if king.row == piece.row:
            left, right = (piece, king) if piece.col < king.col else (king, piece)
            for col in range(left.col+1, right.col):
                if board[piece.row][col] != '.':
                    return False
            return True
        if king.col == piece.col:
            top, botom = (piece, king) if piece.row < king.row else (king, piece)
            for row in range(top.row+1, botom.row):
                if board[row][piece.col] != '.':
                    return False
            return True

    return False

game = 0
while True:
    board = []
    empty = 0
    for _ in range(8):
        row = input()
        if row == '........':
            empty += 1
        board.append(list(row))

    if empty == 8:
        break
    else:
        input()

    k, K = None, None
    for r in range(8):
        for c in range(8):
            if board[r][c] == 'k':
                k = Piece('k', r, c)
            if board[r][c] == 'K':
                K = Piece('K', r, c)
            if board[r][c] != '.':
                board[r][c] = Piece(board[r][c], r, c)

    game += 1
    check = False
    for row in board:
        for piece in row:
            if piece not in ['.', k, K]:
                if piece.rank.islower():
                    if capture_moves(piece, K):
                        print('Game #{}: white king is in check.'.format(game))
                        check = True
                        break
                elif piece.rank.isupper():
                    if capture_moves(piece, k):
                        print('Game #{}: black king is in check.'.format(game))
                        check = True
                        break
        if check:
            break

    if not check:
        print('Game #{}: no king is in check.'.format(game))


