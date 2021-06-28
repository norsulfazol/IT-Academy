from abc import abstractmethod


class Board:
    fig_types = ('', 'Л', 'К', 'С', 'Ф', 'Кр')

    def __init__(self):
        self.protocol = []
        self.del_fig_w = []
        self.del_fig_b = []
        # Послание всем, кто это увидит:
        # Дорогой друг, запомни: X это не X, - это Y
        #                        Y это не Y, - это X
        # Всё не то, чем кажется на самом деле...
        self.board = [[0] * 8 for _ in range(8)]
        for x, i in enumerate('87654321'):
            for y, j in enumerate('abcdefgh'):
                if i in '81':
                    if j in 'ah':
                        self.board[x][y] = Rook()
                    elif j in 'bg':
                        self.board[x][y] = Knight()
                    elif j in 'cf':
                        self.board[x][y] = Bishop()
                    elif j == 'd':
                        self.board[x][y] = Queen()
                    elif j == 'e':
                        self.board[x][y] = King()
                    self.board[x][y].x = x
                    self.board[x][y].y = y
                    self.board[x][y].color = 'wb'[i == '8']
                elif i in '72':
                    self.board[x][y] = Pawn(x=x, y=y, color='wb'[i == '7'])

    def move(self, current, new):
        i = '-'
        fig_type = self.board[current[0]][current[1]].fig_type
        if self.board[new[0]][new[1]]:
            i = 'х'
            if self.board[new[0]][new[1]].color == 'w':
                self.del_fig_w.append(self.board[new[0]][new[1]])
            elif self.board[new[0]][new[1]].color == 'b':
                self.del_fig_b.append(self.board[new[0]][new[1]])
            else:
                self.del_fig_b.append(self.board[new[0]][new[1]])
        if not self.board[current[0]][current[1]].fig_type:
            self.board[current[0]][current[1]].first_move = False
        self.board[new[0]][new[1]], self.board[current[0]][current[1]] = self.board[current[0]][current[1]], 0
        self.board[new[0]][new[1]].x, self.board[new[0]][new[1]].y = new[0], new[1]
        self.protocol.append(f'{fig_type}{ChessPiece.to_fide([current[0], current[1]])}{i}{ChessPiece.to_fide([new[0], new[1]])}')
        # print(self.protocol)

    def set_pawn2queen(self, pawn_obj):
        self.board[pawn_obj.x][pawn_obj.y] = Queen(x=pawn_obj.x, y=pawn_obj.y, color=pawn_obj.color)
        return self.board[pawn_obj.x][pawn_obj.y]


class ChessPiece:
    def __init__(self, x=None, y=None, color=None):
        self.x = x
        self.y = y
        self.color = color
        self.fig_type = ''

    def __str__(self):
        return f'{"White" if self.color == "w" else "Black"} {self.__class__.__name__.lower()} at {self.x, self.y}'

    def __repr__(self):
        return f'{"White" if self.color == "w" else "Black"} {self.__class__.__name__.lower()} at {self.x, self.y}'

    def is_pawn2queen(self):
        return False

    @abstractmethod
    def legal_moves(self, board):
        pass

    @staticmethod
    def from_fide(step):
        return ['87654321'.index(step[1]), 'abcdefgh'.index(step[0])]

    @staticmethod
    def to_fide(step):
        return 'abcdefgh'[step[1]] + '87654321'[step[0]]

    @staticmethod
    def move_check(your_color, x, y, board):
        if x < 0 or x > 7 or y < 0 or y > 7:
            return False, False
        piece = board.board[x][y]
        if piece == 0:
            return True, False
        else:
            if piece.color != your_color:
                return True, True
            else:
                return False, False


class Rook(ChessPiece):
    def __init__(self, **kwds):
        super().__init__(**kwds)
        self.fig_type = 'Л'

    def legal_moves(self, board):
        legal_moves_list = []
        increments = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for offset in increments:
            new_x = self.x
            new_y = self.y
            while True:
                new_x += offset[0]
                new_y += offset[1]
                can_move, capture = self.move_check(self.color, new_x, new_y, board)
                if can_move:
                    legal_moves_list.append(self.to_fide([new_x, new_y]))
                    if capture:
                        break
                else:
                    break
        return legal_moves_list


class Knight(ChessPiece):
    def __init__(self, **kwds):
        super().__init__(**kwds)
        self.fig_type = 'К'

    def legal_moves(self, board):
        legal_moves_list = []
        increments = [[2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1]]
        for offset in increments:
            new_x = self.x + offset[0]
            new_y = self.y + offset[1]
            can_move, capture = self.move_check(self.color, new_x, new_y, board)
            if can_move:
                legal_moves_list.append(self.to_fide([new_x, new_y]))

        return legal_moves_list


class Bishop(ChessPiece):
    def __init__(self, **kwds):
        super().__init__(**kwds)
        self.fig_type = 'С'

    def legal_moves(self, board):
        legal_moves_list = []
        increments = [[-1, -1], [1, 1], [1, -1], [-1, 1]]
        for offset in increments:
            new_x = self.x
            new_y = self.y
            while True:
                new_x += offset[0]
                new_y += offset[1]
                can_move, capture = self.move_check(self.color, new_x, new_y, board)
                if can_move:
                    legal_moves_list.append(self.to_fide([new_x, new_y]))
                    if capture:
                        break
                else:
                    break
        return legal_moves_list


class Queen(ChessPiece):
    def __init__(self, **kwds):
        super().__init__(**kwds)
        self.fig_type = 'Ф'

    def legal_moves(self, board):
        legal_moves_list = []
        increments = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, 1], [1, -1], [1, 1], [-1, -1]]
        for offset in increments:
            new_x = self.x
            new_y = self.y
            while True:
                new_x += offset[0]
                new_y += offset[1]
                can_move, capture = self.move_check(self.color, new_x, new_y, board)
                if can_move:
                    legal_moves_list.append(self.to_fide([new_x, new_y]))
                    if capture:
                        break
                else:
                    break
        return legal_moves_list


class King(ChessPiece):
    def __init__(self, **kwds):
        super().__init__(**kwds)
        self.fig_type = 'Кр'

    def legal_moves(self, board):
        self.board = board
        legal_moves_list = []
        self.moves_temp = []
        increments = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, 1], [1, -1], [1, 1], [-1, -1]]
        for i in range(8):
            for k in range(8):
                if self.board.board[i][k] and self.board.board[i][k].color != self.color and self.board.board[i][k].fig_type != 'Кр' and \
                        self.board.board[i][k].fig_type:
                    if self.board.board[i][k].legal_moves(self.board):
                        self.moves_temp = self.moves_temp + self.board.board[i][k].legal_moves(self.board)
                elif self.board.board[i][k] and self.board.board[i][k].color != self.color and not self.board.board[i][k].fig_type:
                    self.board.board[i][k].legal_moves(self.board)
                    self.moves_temp = self.moves_temp + self.board.board[i][k].attack_moves
        self.moves_temp = list(set(self.moves_temp))

        for offset in increments:
            new_x = self.x + offset[0]
            new_y = self.y + offset[1]
            can_move, capture = self.move_check(self.color, new_x, new_y, board)
            if can_move:
                if self.to_fide([new_x, new_y]) not in self.moves_temp:
                    legal_moves_list.append(self.to_fide([new_x, new_y]))

        return legal_moves_list


class Pawn(ChessPiece):
    def __init__(self, **kwds):
        super().__init__(**kwds)
        self.first_move = True
        self.fig_type = ''

    def legal_moves(self, board):
        self.board = board
        legal_moves_list = []
        self.attack_moves = []
        i = (1, -1)[self.color == 'w']
        if 0 <= (self.x + i) <= 7:
            if (0 <= (self.y + 1) <= 7) and self.board.board[self.x + i][self.y + 1] and (
                    self.board.board[self.x + i][self.y + 1].color != self.board.board[self.x][self.y].color):
                legal_moves_list.append(self.to_fide([self.x + i, self.y + 1]))
            if (0 <= (self.y - 1) <= 7) and self.board.board[self.x + i][self.y - 1] and (
                    self.board.board[self.x + i][self.y - 1].color != self.board.board[self.x][self.y].color):
                legal_moves_list.append(self.to_fide([self.x + i, self.y - 1]))
            if not self.board.board[self.x + i][self.y]:
                legal_moves_list.append(self.to_fide([self.x + i, self.y]))
        if self.first_move:
            if not self.board.board[self.x + i * 2][self.y] and not self.board.board[self.x + i][self.y]:
                legal_moves_list.append(self.to_fide([self.x + i * 2, self.y]))
        if 0 <= (self.x + i) <= 7:
            if 0 <= (self.y - 1) <= 7:
                self.attack_moves += [self.to_fide([self.x + i, self.y - 1])]
            if 0 <= (self.y + 1) <= 7:
                self.attack_moves += [self.to_fide([self.x + i, self.y + 1])]
        return legal_moves_list

    def is_pawn2queen(self):
        if any([all([self.color == 'w', self.x == 0]), all([self.color == 'b', self.x == 7])]):
            return True
        return False


class Game:
    def __init__(self, board):
        self.board = board

    def start(self):
        while True:
            self.w_pos = []
            self.b_pos = []
            self.position()
            i = True
            while i:
                a = input(f'Ход белых, выберите фигуру {self.w_pos}:')
                if a in self.w_pos:
                    if self.board.board[ChessPiece.from_fide(a)[0]][ChessPiece.from_fide(a)[1]].legal_moves(self.board):
                        b = input(f'Куда ходим? {self.board.board[ChessPiece.from_fide(a)[0]][ChessPiece.from_fide(a)[1]].legal_moves(self.board)}:')
                        if b in self.board.board[ChessPiece.from_fide(a)[0]][ChessPiece.from_fide(a)[1]].legal_moves(self.board):
                            self.board.move(ChessPiece.from_fide(a), ChessPiece.from_fide(b))
                            i = False
                        else:
                            print('Эта фигура не может сделать такой ход')
                    else:
                         print('У этой фигуры нет доступных ходов')
            i = True
            while i:
                c = input(f'Ход черных, выберите фигуру {self.b_pos}:')
                if c in self.b_pos:
                    if self.board.board[ChessPiece.from_fide(c)[0]][ChessPiece.from_fide(c)[1]].legal_moves(self.board):
                        d = input(f'Куда ходим? {self.board.board[ChessPiece.from_fide(c)[0]][ChessPiece.from_fide(c)[1]].legal_moves(self.board)}:')
                        if d in self.board.board[ChessPiece.from_fide(c)[0]][ChessPiece.from_fide(c)[1]].legal_moves(self.board):
                            self.board.move(ChessPiece.from_fide(c), ChessPiece.from_fide(d))
                            i = False
                        else:
                            print('Эта фигура не может сделать такой ход')
                    else:
                        print('У этой фигуры нет доступных ходов')

    def position(self):
        for i in self.board.board:
            for j in i:
                if j:
                    getattr(self, f'{j.color}_pos').append(ChessPiece.to_fide([j.x, j.y]))


if __name__ == '__main__':
    b = Board()
    # for x in b.board:
    #     print('-' * 20)
    #     for y in x:
    #         print(y)
    g = Game(b)
    g.start()
