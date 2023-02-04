import sys
import chess
from chessboard import display

def evaluate(board) :
    if board.is_checkmate() :
        if board.turn :
            return -9999
        else :
            return 9999
    if board.is_stalemate() or board.is_insufficient_material() :
        return 0

    material = 0
    piece_tables = {chess.PAWN : 100, chess.KNIGHT : 320, chess.BISHOP : 330, chess.ROOK : 500, chess.QUEEN : 900}
    for piece_type in piece_tables :
        material += len(board.pieces(piece_type, chess.WHITE)) * piece_tables[piece_type]
        material -= len(board.pieces(piece_type, chess.BLACK)) * piece_tables[piece_type]

    return material if board.turn else -material


def move_ordering(position, depth_) :
    """Returns a list of legal moves in order of increasing value"""
    legal_moves = list(position.legal_moves)
    legal_moves.sort(key=lambda move : evaluate(position.copy().push(move)))
    return legal_moves


def alphabeta(position, depth_, alpha=-float('inf'), beta=float('inf')) :
    """Returns [eval, best move] for the position at the given depth"""

    if depth_ == 0 or position.is_game_over() :
        return [evaluate(position), None]

    best_move = None
    for _move in move_ordering(position, depth_) :
        position.push(_move)
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

while not board.is_game_over():
    x = {True : "White's turn", False : "Black's turn"}
    move = input('Enter move:')
    board.push_san(move)
    engine = alphabeta(board, _depth)
    board.push(engine[1])
    print(f"{board}\n", f"Evaluation: {-engine[0]}", f"Best move: {engine[1]}", f"Fen: {board.fen()}",
          f"Turn: {x[board.turn]}", sep='\n')
    game_board = display.start()
    display.update(board.fen(), game_board)
    display.check_for_quit()
else :
    display.terminate()
    print('Game over')
sys.exit()
