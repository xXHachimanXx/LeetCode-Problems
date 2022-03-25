# docs: https://docs.google.com/document/d/1kgHgVX_EUJTeUqyjJwtNa211FtuGef7FbOtg8MZaJqA/edit
def cell_wiil_be_live_or_die( num_live_neigh, cell):
    resp = 0
    
    
    if cell == 1:
        if num_live_neigh == 2 or num_live_neigh == 3:
            resp = 1
    elif cell == 0:
        if num_live_neigh == 3:
            resp = 1
        
    return resp	


def the_game_of_life_1st_step( matrix):
    steps = [
        [0,   1],
        [1,   1],
        [1,   0],
        [1,  -1],
        [0,  -1],
        [-1, -1],
        [-1, 0],
        [-1, 1]
    ]
    next_state = [ [0] * len(matrix[0]) ] * len(matrix) # NxM

    def count_neighbors(row, column):
        live_neigh = 0

        for step in steps:
            x_step = row + step[0]
            y_step = column + step[1]

            if x_step >= 0 and x_step < len(matrix) and y_step >= 0 and y_step < len(matrix[0]):
                if matrix[x_step][y_step] == 1:
                    live_neigh += 1
        return live_neigh 

    decisions = []
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            num_live_neigh = count_neighbors(row, column)
            cell = matrix[row][column]

            decisions.append([num_live_neigh, cell])

    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            num_live_neigh, cell = decisions.pop(0)
            
            matrix[row][column] = cell_wiil_be_live_or_die(num_live_neigh, cell)
    
    return matrix

assert the_game_of_life_1st_step([
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]) == [
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]