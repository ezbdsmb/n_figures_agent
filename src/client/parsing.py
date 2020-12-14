import re

from chess.board import Board


def parse_board(message):
    b = Board()
    fig_info = re.findall(r'\([a-zA-Z]*\d* \d \d\)', message)
    for info in fig_info:
        info = info.replace('(', '').replace(')', '').split()
        b.add_figure(info[0], int(info[1]), int(info[2]))
    return b

