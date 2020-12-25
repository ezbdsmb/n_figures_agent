from chess.board import Board
from chess.under_atack_rules import queen_cells_under_attack
from client.parsing import *
from client.udpclient import UDPClient


class Agent(UDPClient):
    def __init__(self, server_addr):
        super().__init__()

        self.server_addr = server_addr
        self.judge_addr = None

        self.name = None
        self.board = None
        self.width = 0
        self.height = 0

    # TODO: change 8-8 to width-height
    def send_collisions(self):
        cells = []
        for i in range(self.board.width):
            for j in range(self.board.height):
                if self.board.board[i][j] == self.name:
                    cells = queen_cells_under_attack((i, j), self.width, self.height)

        problems = []
        for i in range(self.board.width):
            for j in range(self.board.height):
                if self.board.board[i][j] != '-' and self.board.board[i][j] != self.name and (i, j) in cells:
                    problems.append(self.board.board[i][j])

        mes = ''
        for p in problems:
            mes += p
            mes += ' '
        self.sendto(mes, self.judge_addr)
        print(mes)

    def run(self):
        # send init
        self.sendto("init queen", self.server_addr)
        print('send: init queen')

        # receive init name
        data, addr = self.recvfrom()
        self.name = parse_name(data)
        print('received:', data)

        # receive judge
        data, addr = self.recvfrom()
        self.width, self.height = parse_board_size(data)
        self.judge_addr = addr
        print('received:', data)

        while True:
            # receive board
            data, addr = self.recvfrom()
            self.board = parse_board(data, self.width, self.height)  # TODO: make update, not rewrite
            print('received:', data)

            print(self.name)
            print(self.board)

            # send collision
            self.send_collisions()


if __name__ == '__main__':
    agent1 = Agent(("localhost", 9998))
    agent1.run()
