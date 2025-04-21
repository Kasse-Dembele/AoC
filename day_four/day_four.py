

# TODO:
# - Refactor the code to improve readability and maintainability
# - Replace loop variables (i, j) with descriptive names
# - Define constants for pattern strings ("XMAS", "SAMX") and other magic numbers
# - Use meaningful variable names instead of generic ones like "some_count"

def explore_grid_lines(grid):
    """
    Explores each row in the grid, counting occurrences of "XMAS" and "SAMX" patterns.
    
    Args:
        grid: 2D grid of characters
        
    Returns:
        The total count of "XMAS" and "SAMX" patterns found in all rows
    """
    some_count = 0
    for line in grid:
        line_tex =''.join(line)
        xmas_count = line_tex.count("XMAS")
        samx_count = line_tex.count("SAMX")
        some_count += xmas_count + samx_count
    return some_count

def explore_grid_columns(grid):
    """
    Explores each column in the grid, counting occurrences of "XMAS" and "SAMX" patterns.
    
    Args:
        grid: 2D grid of characters
        
    Returns:
        The total count of "XMAS" and "SAMX" patterns found in all columns
    """
    some_count = 0
    for i in range(len(grid[0])):
        column = [row[i] for row in grid]
        line_tex =''.join(column)
        xmas_count = line_tex.count("XMAS")
        samx_count = line_tex.count("SAMX")
        some_count += xmas_count + samx_count
    return some_count

def explore_grid_diagonal(grid, row_index, column_index):
    """
    Explores a diagonal path from the given starting position (row_index, column_index)
    moving down and right, counting occurrences of "XMAS" and "SAMX" patterns.
    
    Args:
        grid: 2D grid of characters
        row_index: Starting row index
        column_index: Starting column index
        
    Returns:
        The total count of "XMAS" and "SAMX" patterns found in the diagonal
    """
    i = row_index
    j = column_index
    diagonal_chars = []
    while i < len(grid) and j < len(grid[i]):
        diagonal_chars.append(grid[i][j])
        i += 1
        j += 1
    diagonal_tex =''.join(diagonal_chars)
    xmas_count = diagonal_tex.count("XMAS")
    samx_count = diagonal_tex.count("SAMX")
    return xmas_count + samx_count 

def explore_grid_reverse_diagonal(grid, row_index, column_index):
    """
    Explores a reverse diagonal path from the given starting position (row_index, column_index)
    moving up and right, counting occurrences of "XMAS" and "SAMX" patterns.
    
    Args:
        grid: 2D grid of characters
        row_index: Starting row index
        column_index: Starting column index
        
    Returns:
        The total count of "XMAS" and "SAMX" patterns found in the reverse diagonal
    """
    i = row_index
    j = column_index
    reverse_diagonal_chars = []
    while i < len(grid) and i>=0 and j < len(grid[i]) and j >= 0:
        reverse_diagonal_chars.append(grid[i][j])
        i -= 1
        j += 1
    reverse_diagonal_tex =''.join(reverse_diagonal_chars)
    xmas_count = reverse_diagonal_tex.count("XMAS")
    samx_count = reverse_diagonal_tex.count("SAMX")
    return xmas_count + samx_count 


def explore_grid_diagonals(grid):
    """
    Explores all possible diagonals in the grid from top left to bottom right,
    starting from the leftmost column and the top row.
    
    Args:
        grid: 2D grid of characters
        
    Returns:
        The total count of "XMAS" and "SAMX" patterns found in all diagonals
    """
    i = 0
    j = 1
    count = 0
    while i < len(grid):
        count += explore_grid_diagonal(grid, i, 0)
        i += 1

    while j < len(grid[0]) :
        count += explore_grid_diagonal(grid, 0, j)
        j += 1
    return count

def explore_grid_reverse_diagonals(grid):
    i = len(grid) - 1
    j = len(grid[i]) - 1
    count = 0

    while i >= 0:
        count += explore_grid_reverse_diagonal(grid, i, 0)
        i -= 1

    while j > 0:
        count += explore_grid_reverse_diagonal(grid, len(grid) - 1, j)
        j -= 1
    return count

def explore_grid_all_directions(grid):
    count_lines = explore_grid_lines(grid)
    count_columns = explore_grid_columns(grid)
    count_diagonals = explore_grid_diagonals(grid)
    count_reverse_diagonals = explore_grid_reverse_diagonals(grid)
    return count_lines + count_columns + count_diagonals + count_reverse_diagonals

if __name__ == "__main__":

    with open("input_puzzle.txt", "r") as file:
        lines = file.readlines()
        grid = [list(line.strip()) for line in lines]
        print(grid)
    
    total_count = explore_grid_all_directions(grid)
    print(total_count)
    

