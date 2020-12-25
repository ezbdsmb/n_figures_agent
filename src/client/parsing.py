import re

from chess.board import Board


def parse_board_size(message):
    message = message.replace('(', '').replace(')', '').replace(',', '').split(' ')
    return int(message[1]), int(message[2])


def parse_board(message, width, height):
    b = Board(width, height)
    fig_info = re.findall(r'\([a-zA-Z]*\d* \d* \d*\)', message)
    for info in fig_info:
        info = info.replace('(', '').replace(')', '').split()
        b.add_figure(info[0], int(info[1]), int(info[2]))
    return b


def parse_name(message):
    return message.split(' ')[2]


if __name__ == '__main__':
    print(parse_board('(Q1 0 0)(Q2 1 1)(Q3 0 5)'))
