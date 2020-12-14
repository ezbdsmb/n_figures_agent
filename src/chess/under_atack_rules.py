def rook_cells_under_attack(p, width=8, height=8):
    cells = []
    for i in range(height):
        cells.append((p[0], i))
    for i in range(width):
        cells.append((i, p[1]))
    return cells


# TODO: add width and height parameters
def bishop_cells_under_attack(p):
    cells = []
    for k in range(8):
        if p[0] + k <= 7 and p[1] + k <= 7:
            cells.append((p[0] + k, p[1] + k))
        if p[0] + k <= 7 and p[1] - k >= 0:
            cells.append((p[0] + k, p[1] - k))
        if p[0] - k >= 0 and p[1] - k >= 0:
            cells.append((p[0] - k, p[1] - k))
        if p[0] - k >= 0 and p[1] + k <= 7:
            cells.append((p[0] - k, p[1] + k))
    return cells


def queen_cells_under_attack(p):
    return rook_cells_under_attack(p) + bishop_cells_under_attack(p)
