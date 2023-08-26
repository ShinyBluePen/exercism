"""Minesweeper

https://exercism.org/tracks/python/exercises/minesweeper

credit to @Efeqengmng45:
https://exercism.org/tracks/python/exercises/minesweeper/solutions/Efeqengmng45
@GlennJ's solution was also interesting:
https://exercism.org/tracks/python/exercises/minesweeper/solutions/glennj
"""

def annotate(minefield: list[str]) -> list[str]:
    """Add annotations to empty spaces on a minefiled based on how many nearby mines there are.
    
    :param minefield: - A list of strings which may or may not contain mines {*}.
    :return: - The minefield with empty spaces annotated.
    """
    if not minefield: return []
    MINE = "*"
    SLOT = " "
    width = len(minefield[0])
    height = len(minefield)
    minefield = [list(row) for row in minefield]
    
    for y, row in enumerate(minefield):
        if len(row) != width or any([c not in " *" for c in row]):
            raise ValueError("The board is invalid with current input.")

        # for every SLOT on the board, process it's neighbors to determine
        #   the appropriate annotation
        for x, item in [(x, v) for x, v in enumerate(row) if v == SLOT]:
            neighbors = set((
                (-1, -1), (0, -1), (1, -1), 
                (-1,  0),          (1,  0), 
                (-1,  1), (0,  1), (1,  1)
            ))

            # omit positions outside the board range (bounds)
            if y == 0: 
                neighbors.difference_update(set(((-1, -1), (0, -1), (1, -1))))
            if x == 0: 
                neighbors.difference_update(set(((-1, -1), (-1, 0), (-1, 1))))
            if y == height - 1: 
                neighbors.difference_update(set(((-1,  1), (0,  1), (1,  1))))
            if x == width - 1: 
                neighbors.difference_update(set(((1 , -1), (1 , 0), (1 , 1))))

            # check neighbors for mines and tally how many there are
            total = sum([(minefield[y + c[1]][x + c[0]] == MINE) for c in neighbors])
            
            if total:
                minefield[y][x] = str(total)
                
    return (["".join(row) for row in minefield])
  
