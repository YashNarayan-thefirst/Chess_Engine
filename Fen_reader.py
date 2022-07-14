from pprint import pprint
class Piece:
    def _init_(self,color,type_,image,value):
        self.color = color
        self.type_ = type_
        self.image = image
        self.value = value
'''
wk = Piece('w','king','♔',10000)
wq = Piece('w','queen','♕',900)
wr = Piece('w','rook','♖',500)
wb = Piece('w','bishop','♗',310)
wn = Piece('w','n','♘',290)
wp = Piece('w','pawn','♙',100)
bk= Piece('b','king','♚',10000)
bq = Piece('b','queen','♛',900)
br = Piece('b','rook','♜',500)
bb = Piece('b','bishop','♝',310)
bn = Piece('b','knight','♞',290)
bp = Piece('b','pawn','♟',100)
'''
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
                brow.append( '♟' )
            elif c == 'p':
                brow.append( '♙' )
            elif c=='R':
                brow.append('♜')
            elif c=='N':
                brow.append('♞')
            elif c=='B':
                brow.append('♝')
            elif c=='Q':
                brow.append('♛')
            elif c=='r':
                brow.append('♖')
            elif c=='n':
                brow.append('♘')
            elif c=='b':
                brow.append('♗')
            elif c=='q':
                brow.append('♕')
            elif c=='k':
                brow.append('♔')
            elif c=='K':
                brow.append('♚')

        board.append(brow)
    return board
