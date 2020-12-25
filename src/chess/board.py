class Board:
    def __init__(self, width=8, height=8):
        self.resize(width, height)
        self.width = width
        self.height = height

        self.agents = []

    def __str__(self):
        res = ''
        for row in self.board:
            for el in row:
                res += str(el) + '\t'
            res += '\n'
        return res

    def resize(self, width, height):
        self.board = []
        for i in range(width):
            self.board.append([])
            for j in range(height):
                self.board[i].append('-')

    def add_figure(self, figure, x, y):
        self.board[x][y] = figure


if __name__ == '__main__':
    b = Board(10, 5)
    b.add_figure('R1', 5, 2)
    print(b)
