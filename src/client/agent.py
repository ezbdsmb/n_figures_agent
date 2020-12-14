from chess.board import Board
from chess.under_atack_rules import queen_cells_under_attack
from client.parsing import parse_board
from client.udpclient import UDPClient


class Agent(UDPClient):
    def __init__(self, server_addr):
        super().__init__(server_addr)

        self.name = None
        self.board = None

    # TODO: change 8-8 to width-height
    def send_problems(self):
        cells = []
        for i in range(8):
            for j in range(8):
                if self.board.board[i][j] == self.name:
                    cells = queen_cells_under_attack((i, j))

        problems = []
        for i in range(8):
            for j in range(8):
                if self.board.board[i][j] != '-' and self.board.board[i][j] != self.name and (i, j) in cells:
                    problems.append(self.board.board[i][j])

        print(problems)

    def run(self):
        self.send("init queen")
        self.name = self.recv()

        while True:
            self.board = parse_board(self.recv())  # TODO: make update, not rewrite
            print(self.name)
            print(self.board)
            self.send_problems()


if __name__ == '__main__':
    agent1 = Agent(("localhost", 9999))
    agent1.run()
