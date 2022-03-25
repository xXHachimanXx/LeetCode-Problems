# docs: https://docs.google.com/document/d/1WATZWZLR7s2j72eFvZ7314tvKcg6EbfDfPYDMaYG1F4/edit
def is_Toeplitz_matrix(matrix):
    num_rows = len(matrix)
    num_columns = len(matrix[0])

    for row in range(num_rows-1): # 1
        for column in range(num_columns-1): # 
            # [1, 1] != [2, 2]
            if matrix[row][column] != matrix[row+1][column+1]:
                return False
    return True

assert is_Toeplitz_matrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]) == True
assert is_Toeplitz_matrix([[1,2],[2,2]]) == False