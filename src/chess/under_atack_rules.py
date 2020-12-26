def rook_cells_under_attack(p, width=8, height=8):
    cells = []
    for i in range(height):
        cells.append((p[0], i))
    for i in range(width):
        cells.append((i, p[1]))
    return cells


# TODO: add width and height parameters
def bishop_cells_under_attack(p, width=8, height=8):
    cells = []
    for k in range(max(width, height)):
        if p[0] + k <= width and p[1] + k <= height:
            cells.append((p[0] + k, p[1] + k))
        if p[0] + k <= width and p[1] - k >= 0:
            cells.append((p[0] + k, p[1] - k))
        if p[0] - k >= 0 and p[1] - k >= 0:
            cells.append((p[0] - k, p[1] - k))
        if p[0] - k >= 0 and p[1] + k <= height:
            cells.append((p[0] - k, p[1] + k))
    return cells


def queen_cells_under_attack(p, width=8, height=8):
    return rook_cells_under_attack(p, width, height) + bishop_cells_under_attack(p, width, height)
