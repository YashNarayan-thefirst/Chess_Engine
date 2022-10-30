import random
import sys

import chess


def evaluate() :
    if board.is_checkmate() :
        if board.turn :
            return -9999
        else :
            return 9999
    if board.is_stalemate() :
        return 0
    if board.is_insufficient_material() :
        return 0
    if board.can_claim_fifty_moves():
        return 0
    if board.can_claim_threefold_repetition():
        return 0
    #counts material
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

    material = ((100 * (wp - bp)) + (320 * (wn - bn)) + (330 * (wb - bb)) + (500 * (wr - br)) + (900 * (wq - bq)))/100
    return material

def alphabeta(board,depth,alpha=-float('inf'),beta=float('inf')):

    if depth ==0 or board.is_game_over():
        return [None,evaluate()]
    move_list = list(board.legal_moves)
    best_move = random.choice(move_list)
    if board.turn: #for the current player's turn
        max_eval = -float('inf')
        for _move in move_list:
            board.push_san(str(_move))
            current_eval = alphabeta(board,depth-1,alpha=-float('inf'),beta=float('inf'))[1]
            print({'Position':board,'Evaluation': current_eval}) #Comment this statement to reduce clutter
            board.pop()
            if current_eval>max_eval: #Max score
                max_eval = current_eval
                best_move=_move
            #alpha beta pruning
            alpha = max(alpha,current_eval)
            if beta<=alpha: #White maximises their score beta>=alpha
                break
        return [best_move,max_eval]

    else: #Min score for the opponent
        min_eval = float('inf')
        for _move in move_list:
            board.push_san(str(_move))
            current_eval = alphabeta(board,depth-1,alpha=-float('inf'),beta=float('inf'))[1]
            board.pop()
            if current_eval< min_eval:
                min_eval = current_eval
                best_move =_move
            #Alpha beta pruning
            beta = min(beta, current_eval) #black minimizes their score
            if beta <= alpha:#beta>=alpha
                break
        return [best_move,min_eval]


fen_ = input('Enter fen: ')
board = chess.Board(fen_)
_depth = int(input('Enter depth: '))
engine = alphabeta(board,_depth)
print(board)
print(f'Best move is: {engine[0]}')
print(f'Evaluation is: {engine[1]}')
sys.exit()

    
