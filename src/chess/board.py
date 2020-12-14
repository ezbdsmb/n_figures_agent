class Board:
    def __init__(self):
        self.board = []
        for i in range(8):
            self.board.append([])
            for j in range(8):
                self.board[i].append('-')

        self.agents = []

    def __str__(self):
        res = ''
        for row in self.board:
            for el in row:
                res += str(el) + '\t'
            res += '\n'
        return res

    def add_figure(self, figure, x, y):
        self.board[x][y] = figure


if __name__ == '__main__':
    b = Board()
    b.add_figure('R1', 5, 2)
    print(b)
