import random
from chess_obj import Board, ChessPiece
from time import sleep
from turtle import *

if __name__ == '__main__':
    cell_side_len = 60
    board_font = ('Arial', 10, 'bold')
    board_colors = ['silver', 'grey']
    chess_img_folder = 'chess_img'
    window = Screen()
    window.title('Chess')
    window.screensize(canvwidth=cell_side_len * 10, canvheight=cell_side_len * 10, bg='black')
    window.setup(width=window.screensize()[0] + 20, height=window.screensize()[1] + 20, startx=None, starty=None)
    board_obj = Board()
    board_pen = Turtle()
    for i in board_obj.fig_types:
        for j in 'wb':
            window.addshape(f'{chess_img_folder}/{i}{j}.gif')
    board_pen.pen(shown=False, pendown=False, pensize=1, speed=10)
    cells_coords = []
    chess_pieces = {}
    for n, y in zip(' 87654321 ', range(window.screensize()[1] // 2, -window.screensize()[1] // 2, -cell_side_len)):
        board_pen.sety(y + (0 if n.strip() else (5 if y > 0 else 40) - cell_side_len))
        yy = board_pen.ycor()
        if n.strip():
            cells_coords.append([])
        for a, x in zip(' abcdefgh ', range(-window.screensize()[0] // 2, window.screensize()[0] // 2, cell_side_len)):
            board_pen.sety(yy - (0 if a.strip() else cell_side_len // 2 + 10))
            board_pen.setx(
                x + ((0 if n.strip() else cell_side_len // 2) if a.strip() else (cell_side_len - 10 if x < 0 else 10)))
            board_pen.pd()
            if n.strip():
                if a.strip():
                    board_pen.color('grey', board_colors[0] if (ord(n) + ord(a)) % 2 else board_colors[1])
                    board_pen.begin_fill()
                    board_pen.setx(board_pen.xcor() + cell_side_len)
                    board_pen.sety(board_pen.ycor() - cell_side_len)
                    board_pen.setx(board_pen.xcor() - cell_side_len)
                    board_pen.sety(board_pen.ycor() + cell_side_len)
                    board_pen.end_fill()
                    cells_coords[-1].append((board_pen.xcor() + cell_side_len // 2,
                                             board_pen.ycor() - cell_side_len // 2))
                    cell_coords = ChessPiece.from_fide(f'{a}{n}')
                    chess_piece_obj = board_obj.board[cell_coords[0]][cell_coords[1]]
                    if chess_piece_obj:
                        chess_piece_pen = Turtle()
                        chess_piece_pen.pen(shown=False, pendown=False, pensize=1, speed=10)
                        chess_piece_pen.shape(
                            f'{chess_img_folder}/{chess_piece_obj.fig_type}{chess_piece_obj.color}.gif')
                        chess_piece_pen.goto(*cells_coords[-1][-1])
                        chess_piece_pen.st()
                        chess_piece_pen.speed(1)
                        chess_pieces[chess_piece_obj] = chess_piece_pen
                else:
                    board_pen.color('yellow')
                    board_pen.write(n, align='center', font=board_font)
            else:
                board_pen.color('yellow')
                board_pen.write(a.upper(), align='center', font=board_font)
            board_pen.up()

    chess_pieces_colors = 'wb'
    chess_pieces_available = [k for k in chess_pieces if k.color == chess_pieces_colors[0] and k.legal_moves(board_obj)]
    while chess_pieces_available:
        random_chess_piece = random.choice(chess_pieces_available)
        random_move = ChessPiece.from_fide(random.choice(random_chess_piece.legal_moves(board_obj)))

        print(f'{random_chess_piece} move to {random_move} = {cells_coords[random_move[0]][random_move[1]]}')

        board_obj.move((random_chess_piece.x, random_chess_piece.y), random_move)

        clone_pen = chess_pieces[random_chess_piece].clone()
        chess_pieces[random_chess_piece].ht()
        clone_pen.goto(*cells_coords[random_move[0]][random_move[1]])
        chess_pieces[random_chess_piece] = clone_pen

        for k in list(chess_pieces):
            if k in board_obj.del_fig_w + board_obj.del_fig_b:
                chess_pieces.pop(k).ht()

        if random_chess_piece.is_pawn2queen():
            chess_piece_obj = board_obj.set_pawn2queen(random_chess_piece)
            clone_pen = chess_pieces[random_chess_piece].clone()
            clone_pen.shape(f'{chess_img_folder}/{chess_piece_obj.fig_type}{chess_piece_obj.color}.gif')
            chess_pieces[random_chess_piece].ht()
            del chess_pieces[random_chess_piece]
            chess_pieces[chess_piece_obj] = clone_pen

        chess_pieces_colors = chess_pieces_colors[::-1]
        chess_pieces_available = [k for k in chess_pieces if
                                  k.color == chess_pieces_colors[0] and k.legal_moves(board_obj)]

    board_font = ('Arial', 20, 'bold')
    board_pen.goto(0, -14)
    board_pen.color('blue')
    board_pen.write('Happy end', align='center', font=board_font)
    sleep(1.5)
    board_pen.undo()
    board_pen.color('red')
    board_pen.write('GAME OVER', align='center', font=board_font)
    sleep(2)
    window.bye()
