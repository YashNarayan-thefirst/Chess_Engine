import chess
import sys
import chessboard
from chessboard import display

piece_tables = {chess.PAWN : 100, chess.KNIGHT : 320, chess.BISHOP : 330, chess.ROOK : 500, chess.QUEEN : 900,
                chess.KING : 0}
piece_square_tables = {
    chess.PAWN : [
        0, 0, 0, 0, 0, 0, 0, 0,
        50, 50, 50, 50, 50, 50, 50, 50,
        10, 10, 20, 30, 30, 20, 10, 10,
        5, 5, 10, 25, 25, 10, 5, 5,
        0, 0, 0, 20, 20, 0, 0, 0,
        5, -5, -10, 0, 0, -10, -5, 5,
        5, 10, 10, -20, -20, 10, 10, 5,
        0, 0, 0, 0, 0, 0, 0, 0
    ],
    chess.KNIGHT : [
        -50, -40, -20, -30, -30, -20, -40, -50,
        -40, -20, 0, 0, 0, 0, -20, -40,
        -30, 0, 10, 15, 15, 10, 0, -30,
        -30, 5, 15, 20, 20, 15, 5, -30,
        -30, 0, 15, 20, 20, 15, 0, -30,
        -30, 5, 5, 15, 15, 5, 5, -30,
        -40, -20, 0, 5, 5, 0, -20,-40,
        -50, -40, -20, -30, -30, -20, -40, -50
    ],
    chess.BISHOP : [
        -20, -10, -10, -10, -10, -10, -10, -20,
        -10, 0, 0, 0, 0, 0, 0, -10,
        -10, 0, 5, 10, 10, 5, 0, -10,
        -10, 5, 5, 10, 10, 5, 5, -10,
        -10, 0, 10, 10, 10, 10, 0, -10,
        -10, 10, 10, 10, 10, 10, 10, -10,
        -10, 5, 0, 0, 0, 0, 5, -10,
        -20, -10, -40, -10, -10, -40, -10, -20
    ],
    chess.ROOK : [
        0, 0, 0, 0, 0, 0, 0, 0,
        5, 10, 10, 10, 10, 10, 10, 5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        0, 0, 0, 5, 5, 0, 0, 0
    ],
    chess.QUEEN : [
        -20, -10, -10, -5, -5, -10, -10, -20,
        -10, 0, 0, 0, 0, 0, 0, -10,
        -10, 0, 5, 5, 5, 5, 0, -10,
        -5, 0, 5, 5, 5, 5, 0, -5,
        0, 0, 5, 5, 5, 5, 0, -5,
        -10, 5, 5, 5, 5, 5, 0, -10,
        -10, 0, 5, 0, 0, 0, 0, -10,
        -20, -10, -10, -5, -5, -10, -10, -20
    ],
    chess.KING:[5, 5, -30, -55, -55, -30, 5, 5, 50, 5, -30, -55, -55, -30, 5, 50, 50, 50, -10, -55, -55, -10, 50, 50, 50, 50, -10, -55, -55, -10, 50, 50, 50, 50, -10, -55, -55, -10, 50, 50, 50, 50, -10, -55, -55, -10, 50, 50, 50, 50, -10, -55, -55, -10, 50, 50, 50, 50, -10, -55, -55, -10, 50, 50, 50, 50, -10, -55, -55, -10, 50, 50, 50, 50, -10, -55, -55, -10, 50, 50, 50, 50, -10, -55, -55, -10, 50, 50, 50, 50, -10, -55, -55, -10, 50, 50, 50, 50, -10, -55, -55, -10, 50, 50, 50, 50, -10, -55, -55, -10, 50, 50, 50, 50, -10, -55, -55, -10, 50, 50, 50, 50, -10, -55, -55, -10, 50, 50, 50, 50, -10, -55, -55, -10, 50, 50, 50, 50, -10, -55, -55, -10, 50, 50, 50, 50, -10, -55, -55, -10, 50, 50, 50, 50, -10, -55, -55, -10, 50, 50, 50, 50, -10, -55, -55, -10, 50, 50, 50, 50, -10, -55, -55, -10, 50, 50, 50, 50, -10, -55, -55, -10, 50, 50, 50, 50, -10, -55, -55, -10, 50, 50, 50, 50, -10, -55, -55, -10, 50, 50, 50, 50, -10, -55, -55, -10, 50, 50, 50, 50, -10, -55, -55, -10, 50, 50, 50, 50, -10, -55, -55, -10, 50, 50, 50, 50, -10, -55, -55, -10, 50]
}

center_control_tables = {
    chess.A1 : 1,
    chess.A2 : 1,
    chess.A3 : 1,
    chess.A4 : 1,
    chess.A5 : 1,
    chess.A6 : 1,
    chess.A7 : 1,
    chess.A8 : 1,
    chess.B1 : 1,
    chess.B2 : 1,
    chess.B3 : 1,
    chess.B4 : 1,
    chess.B5 : 1,
    chess.B6 : 1,
    chess.B7 : 1,
    chess.B8 : 1,
    chess.C1 : 5,
    chess.C2 : 5,
    chess.C3 : 5,
    chess.C4 : 5,
    chess.C5 : 5,
    chess.C6 : 5,
    chess.C7 : 5,
    chess.C8 : 5,
    chess.D1 : 10,
    chess.D2 : 10,
    chess.D3 : 3,
    chess.D4 : 10,
    chess.D5 : 10,
    chess.D6 : 3,
    chess.D7 : 10,
    chess.D8 : 10,
    chess.E1 : 10,
    chess.E2 : 10,
    chess.E3 : 3,
    chess.E4 : 10,
    chess.E5 : 10,
    chess.E6 : 3,
    chess.E7 : 10,
    chess.E8 : 10,
    chess.F1 : 5,
    chess.F2 : 5,
    chess.F3 : 5,
    chess.F4 : 5,
    chess.F5 : 5,
    chess.F6 : 4,
    chess.F7 : 5,
    chess.F8 : 5,
    chess.G1 : 1,
    chess.G2 : 1,
    chess.G3 : 1,
    chess.G4 : 1,
    chess.G5 : 1,
    chess.G6 : 1,
    chess.G7 : 1,
    chess.G8 : 1,
    chess.H1 : 1,
    chess.H2 : 1,
    chess.H3 : 1,
    chess.H4 : 1,
    chess.H5 : 1,
    chess.H6 : 1,
    chess.H7 : 1,
    chess.H8 : 1,
}

pawn_structure_tables = {
    chess.A1: -10, chess.A2: -10, chess.A3: 0, chess.A4: 5, chess.A5: 5, chess.A6: 0, chess.A7: -10, chess.A8: -10,
    chess.B1: -5, chess.B2: -5, chess.B3: 0, chess.B4: 0, chess.B5: 0, chess.B6: 0, chess.B7: -5, chess.B8: -5,
    chess.C1: 0, chess.C2: 0, chess.C3: 0, chess.C4: 0, chess.C5: 0, chess.C6: 0, chess.C7: 0, chess.C8: 0,
    chess.D1: 5, chess.D2: 5, chess.D3: 0, chess.D4: 0, chess.D5: 0, chess.D6: 0, chess.D7: 5, chess.D8: 5,
    chess.E1: 5, chess.E2: 5, chess.E3: 0, chess.E4: 0, chess.E5: 0, chess.E6: 0, chess.E7: 5, chess.E8: 5,
    chess.F1: 0, chess.F2: 0, chess.F3: 0, chess.F4: 0, chess.F5: 0, chess.F6: 0, chess.F7: 0, chess.F8: 0,
    chess.G1: -5, chess.G2: -5, chess.G3: 0, chess.G4: 0, chess.G5: 0, chess.G6: 0, chess.G7: -5, chess.G8: -5,
    chess.H1: -10, chess.H2: -10, chess.H3: 0, chess.H4: 5, chess.H5: 5, chess.H6: 0, chess.H7: -10, chess.H8: -10,
}
king_safety_tables = {
    chess.A1: 0, chess.B1: 0, chess.C1: 0, chess.D1: 1,
    chess.E1: 2, chess.F1: 0, chess.G1: 0, chess.H1: 0,
    chess.A2: 1, chess.B2: 1, chess.C2: 1, chess.D2: 1,
    chess.E2: 1, chess.F2: 1, chess.G2: 1, chess.H2: 1,
    chess.A3: 2, chess.B3: 2, chess.C3: 2, chess.D3: 2,
    chess.E3: 2, chess.F3: 2, chess.G3: 2, chess.H3: 2,
    chess.A4: 3, chess.B4: 3, chess.C4: 3, chess.D4: 3,
    chess.E4: 3, chess.F4: 3, chess.G4: 3, chess.H4: 3,
    chess.A5: 4, chess.B5: 4, chess.C5: 4, chess.D5: 4,
    chess.E5: 4, chess.F5: 4, chess.G5: 4, chess.H5: 4,
    chess.A6: 5, chess.B6: 5, chess.C6: 5, chess.D6: 5,
    chess.E6: 5, chess.F6: 5, chess.G6: 5, chess.H6: 5,
    chess.A7: 6, chess.B7: 6, chess.C7: 6, chess.D7: 6,
    chess.E7: 6, chess.F7: 6, chess.G7: 6, chess.H7: 6,
    chess.A8: 7, chess.B8: 7, chess.C8: 7, chess.D8: 8,
    chess.E8: 9, chess.F8: 7, chess.G8: 7, chess.H8: 7,
}
endgame_tables = {
    chess.A1: 0, chess.B1: 0, chess.C1: 0, chess.D1: 0, chess.E1: 0, chess.F1: 0, chess.G1: 0, chess.H1: 0,
    chess.A2: 5, chess.B2: 10, chess.C2: 10, chess.D2: 10, chess.E2: 10, chess.F2: 10, chess.G2: 10, chess.H2: 5,
    chess.A3: 4, chess.B3: 8, chess.C3: 8, chess.D3: 8, chess.E3: 8, chess.F3: 8, chess.G3: 8, chess.H3: 4,
    chess.A4: 3, chess.B4: 6, chess.C4: 6, chess.D4: 6, chess.E4: 6, chess.F4: 6, chess.G4: 6, chess.H4: 3,
    chess.A5: 2, chess.B5: 4, chess.C5: 4, chess.D5: 4, chess.E5: 4, chess.F5: 4, chess.G5: 4, chess.H5: 2,
    chess.A6: 1, chess.B6: 2, chess.C6: 2, chess.D6: 2, chess.E6: 2, chess.F6: 2, chess.G6: 2, chess.H6: 1,
    chess.A7: 0, chess.B7: 0, chess.C7: 0, chess.D7: 0, chess.E7: 0, chess.F7: 0, chess.G7: 0, chess.H7: 0,
    chess.A8: 0, chess.B8: 0, chess.C8: 0, chess.D8: 0, chess.E8: 0, chess.F8: 0, chess.G8: 0, chess.H8: 0,
}


def evaluate(position) :
    if position is not None:
        if position.is_checkmate() :
            if position.turn :
                return -999900
            else :
                return 999900
        if position.is_stalemate() or position.is_insufficient_material() :
            return 0
        total_evaluation = 0
        for square in chess.SQUARES :
            piece = position.piece_at(square)
            if piece :
                piece_value = piece_tables[piece.piece_type]
                if not piece.color :
                    piece_value *= -1
                else :
                    piece_value += piece_square_tables[piece.piece_type][square]
                total_evaluation += piece_value

        # pawn structure score
        pawns = position.pieces(chess.PAWN, position.turn)
        pawn_structure_score = sum([pawn_structure_tables[square] for square in pawns])
        total_evaluation += pawn_structure_score

        # king safety score
        own_king_square = position.king(position.turn)
        own_king_safety_score = king_safety_tables[own_king_square]
        opponent_king_square = position.king(not position.turn)
        opponent_king_safety_score = king_safety_tables[opponent_king_square]
        total_evaluation += (own_king_safety_score - opponent_king_safety_score)

        # mobility score
        own_legal_moves = position.legal_moves.count()
        opponent_legal_moves = position.legal_moves.count()
        mobility_score = own_legal_moves - opponent_legal_moves
        mobility_score/=10
        total_evaluation += mobility_score

        # center control score
        own_center_control = sum([1 for square in center_control_tables if position.attackers(position.turn, square)])
        opponent_center_control = sum([1 for square in center_control_tables if position.attackers(not position.turn, square)])
        center_control_score = center_control_tables[own_center_control] - center_control_tables[opponent_center_control]
        center_control_score/=10
        total_evaluation+= center_control_score

        endgame_score = 0
        endgame_threshold= 10

        if total_evaluation <= endgame_threshold :
            endgame_score = endgame_tables[own_center_control] - endgame_tables[opponent_center_control]

        total_evaluation += endgame_score
        return total_evaluation
    else:
        return 0

def move_ordering(position) :
    """Returns a list of legal moves in order of increasing value"""
    legal_moves = list(position.legal_moves)
    legal_moves.sort(key=lambda move : evaluate(position.copy().push(move)))
    return legal_moves

def alphabeta(position, depth_, alpha=-float('inf'), beta=float('inf')) :
    """Returns [eval, best move] for the position at the given depth"""

    if depth_ == 0 or position.is_game_over() :
        return [evaluate(position), None]

    best_move = None
    for _move in move_ordering(position) :
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

while True:
    game_board = display.start()
    if not board.is_game_over():
        try:
            display.update(board.fen(), game_board)
            x = {True : "White's turn", False : "Black's turn"}
            move = input('Enter move:')
            board.push_san(str(move))
            engine = alphabeta(board, _depth)
            board.push(engine[1])
            print(f"{board}\n", f"Evaluation: {-engine[0]/100}", f"Best move: {engine[1]}", f"Fen: {board.fen()}",
                  f"Turn: {x[board.turn]}", sep='\n')
            display.update(board.fen(), game_board)
            display.check_for_quit()
        except:
            print('Game over', f'Result: {board.result()}')
            break
    else:
        print(f'Game over\nResult: {board.result()}')
        break
