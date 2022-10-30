# Chess_Engine
A chess engine in python
'''
Project by Yash Narayan
Fen is a string which indicates the current position of the board. Ex: starting fen is rnbqkbnr/pppppppp/8/8/8/8/PPPPPPP
P/RNBQKBNR w KQkq - 0 1
It also only gives 1 move as the best move, not the continuation. 
Depth is an int which determines how far ahead it can look, the more the depth, the more computational power is required
(depth should not be >10, since this isn't very optimised.)
Test positions:
M1: 1rb1kbr1/p4n1p/1p2pB2/1Np5/P7/8/1PP2PPP/3RK2R w K - 4 20
M3: r4r2/pp3pkp/5N2/7Q/4PP2/2PP4/q6P/1R4bK w - - 0 23  (depth>=3)
Draw: qqqqkqqq/qqbbnqqq/qqbpnqqq/qqnnnqqq/qqqnNqqq/qqqqqqqq/qqqnnnqq/qqqnKnqq w - - 0 1

The best move is given in the form [from_square-> to_square]
More on chess coordinates and notation:
https://www.chessprogramming.org/Forsyth-Edwards_Notation
https://en.wikipedia.org/wiki/Universal_Chess_Interface

It has taken around 15 hours of work in total to finish.
'''
