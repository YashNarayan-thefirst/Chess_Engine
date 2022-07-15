import Engine

wk = Engine.GameState.Piece('w', 'king', '♔', 10000)
wq = Engine.GameState.Piece('w', 'queen', '♕', 900)
wr = Engine.GameState.Piece('w', 'rook', '♖', 500)
wb = Engine.GameState.Piece('w', 'bishop', '♗', 310)
wn = Engine.GameState.Piece('w', 'n', '♘', 290)
wp = Engine.GameState.Piece('w', 'pawn', '♙', 100)
bk = Engine.GameState.Piece('b', 'king', '♚', 10000)
bq = Engine.GameState.Piece('b', 'queen', '♛', 900)
br = Engine.GameState.Piece('b', 'rook', '♜', 500)
bb = Engine.GameState.Piece('b', 'bishop', '♝', 310)
bn = Engine.GameState.Piece('b', 'knight', '♞', 290)
bp = Engine.GameState.Piece('b', 'pawn', '♟', 100)

default_fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

def fen_to_board(fen_):
    board = []
    for row in fen_.split('/'):
        brow = []
        for c in row:
            if c == ' ':
                break
            elif c in '12345678':
                brow.extend( ['-'] * int(c) )
            elif c == 'P':
                brow.append(wp)
            elif c == 'p':
                brow.append(bp)
            elif c=='R':
                brow.append(wr)
            elif c=='N':
                brow.append(wn)
            elif c=='B':
                brow.append(wb)
            elif c=='Q':
                brow.append(wq)
            elif c=='r':
                brow.append(br)
            elif c=='n':
                brow.append(bn)
            elif c=='b':
                brow.append(bb)
            elif c=='q':
                brow.append(bq)
            elif c=='k':
                brow.append(bk)
            elif c=='K':
                brow.append(wk)

        board.append(brow)
    return board

