import sys

import chess


def evaluate(position) :
    if board.is_checkmate() :
        if board.turn :
            return -9999
        else :
            return 9999
    if board.is_stalemate() :
        return 0
    if board.is_insufficient_material() :
        return 0

    wp = len(board.pieces(chess.PAWN, chess.WHITE))
    bp = len(board.pieces(chess.PAWN, chess.BLACK))
    wn = len(board.pieces(chess.KNIGHT, chess.WHITE))
    bn = len(board.pieces(chess.KNIGHT, chess.BLACK))
    wb = len(board.pieces(chess.BISHOP, chess.WHITE))
    bb = len(board.pieces(chess.BISHOP, chess.BLACK))
    wr = len(board.pieces(chess.ROOK, chess.WHITE))
    br = len(board.pieces(chess.ROOK, chess.BLACK))
    wq = len(board.pieces(chess.QUEEN, chess.WHITE))
    bq = len(board.pieces(chess.QUEEN, chess.BLACK))

    material = (100 * (wp - bp) + 320 * (wn - bn) + 330 * (wb - bb) + 500 * (wr - br) + 900 * (wq - bq)) / 100
    return material if position.turn else -material


def alphabeta(position, depth_, alpha=-float('inf'), beta=float('inf')) :
    """Returns [eval, best move] for the position at the given depth"""

    if depth_ == 0 or position.is_game_over() :
        return [evaluate(position), None]

    best_move = None
    for _move in position.legal_moves :
        position.push(_move)
        #print({'Position': position,'Evaluation': evaluate(position)})
        score, move_ = alphabeta(position, depth_ - 1, -beta, -alpha)
        score = -score
        position.pop()
        if score > alpha :  # player maximizes his score
            alpha = score
            best_move = _move
            if alpha >= beta :  # alpha-beta cutoff
                break

    return [alpha, best_move]


fen_ = input('Enter fen: ')
board = chess.Board(fen_)
_depth = int(input('Enter depth: '))
'''
#uncomment this if you just want to see the best move
engine = alphabeta(board, _depth)
board.push_san(str(engine[1]))
print(f'{board}', f'Evaluation: {engine[0]}', f'Best move: {engine[1]}', f'Fen: {board.fen()}',sep='\n')

'''
while not board.is_game_over() :
    x = {True: 'White\'s turn',False:'Black\'s Turn'}
    move = input('Enter move:')
    Board.push_san(move)
    engine = alphabeta(board, _depth)
    board.push(engine[1])
    print(f'{board}\n', f'Evaluation: {-engine[0]}', f'Best move: {engine[1]}', f'Fen: {board.fen()}',
          f'Turn: {x[board.turn]}', sep='\n')
    print('\n\n')
else:
    print('Game over')
#'''
sys.exit()
