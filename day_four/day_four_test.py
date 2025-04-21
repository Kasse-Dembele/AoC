
from day_four import explore_grid_lines, explore_grid_columns, explore_grid_diagonal, explore_grid_reverse_diagonal, explore_grid_diagonals, explore_grid_reverse_diagonals

def test_explore_grid_lines():
    grid = [
        ["X", "M", "A", "S", "X"],
        ["M", "A", "S", "X", "M"],
        ["A", "S", "X", "M", "A"],
        ["S", "X", "M", "A", "S"],
    ]
    assert explore_grid_lines(grid) == 2

def test_explore_grid_columns():
    grid = [
        ["X", "M", "A", "S", "S"],
        ["M", "A", "S", "X", "A"],
        ["A", "S", "X", "M", "M"],
        ["S", "X", "M", "A", "X"]
    ]
    assert explore_grid_columns(grid) == 2
    assert explore_grid_columns(grid) == 2

def test_explore_grid_diagonal():
    grid = [
        ["X", "S", "A", "S", "S"],
        ["M", "M", "A", "X", "A"],
        ["A", "S", "A", "M", "M"],
        ["S", "X", "M", "S", "X"]
    ]
    assert explore_grid_diagonal(grid, row_index=0, column_index=0) == 1
    assert explore_grid_diagonal(grid, row_index=0, column_index=1) == 1
    assert explore_grid_diagonal(grid, row_index=0, column_index=2) == 0
    assert explore_grid_diagonal(grid, row_index=0, column_index=3) == 0
    assert explore_grid_diagonal(grid, row_index=0, column_index=4) == 0
    assert explore_grid_diagonal(grid, row_index=1, column_index=0) == 0
    assert explore_grid_diagonal(grid, row_index=1, column_index=1) == 0
    assert explore_grid_diagonal(grid, row_index=1, column_index=2) == 0
    assert explore_grid_diagonal(grid, row_index=1, column_index=3) == 0
    assert explore_grid_diagonal(grid, row_index=1, column_index=4) == 0

def test_explore_grid_reverse_diagonal():
    grid = [
        ["X", "S", "A", "S", "S"],
        ["M", "M", "A", "A", "X"],
        ["A", "S", "M", "M", "M"],
        ["S", "X", "A", "S", "X"],
        ["S", "S", "M", "S", "X"],
    ]
    assert explore_grid_reverse_diagonal(grid, row_index=4, column_index=0) == 1
    assert explore_grid_reverse_diagonal(grid, row_index=3, column_index=0) == 0
    assert explore_grid_reverse_diagonal(grid, row_index=2, column_index=0) == 0
    assert explore_grid_reverse_diagonal(grid, row_index=1, column_index=0) == 0
    assert explore_grid_reverse_diagonal(grid, row_index=0, column_index=0) == 0
    assert explore_grid_reverse_diagonal(grid, row_index=4, column_index=1) == 1
    assert explore_grid_reverse_diagonal(grid, row_index=4, column_index=2) == 0
    assert explore_grid_reverse_diagonal(grid, row_index=4, column_index=3) == 0
    assert explore_grid_reverse_diagonal(grid, row_index=4, column_index=3) == 0
  
def test_explore_grid_diagonals():
    grid = [
        ["X", "S", "A", "S", "S"],
        ["M", "M", "A", "X", "A"],
        ["A", "S", "A", "M", "M"],
        ["S", "X", "M", "S", "X"]
    ]
    assert explore_grid_diagonals(grid) == 2
    
def test_explore_grid_reverse_diagonals():
    grid = [
        ["X", "S", "A", "S", "S"],
        ["M", "M", "A", "A", "X"],
        ["A", "S", "M", "M", "M"],
        ["S", "X", "A", "S", "X"],
        ["S", "S", "M", "S", "X"],
    ]
    assert explore_grid_reverse_diagonals(grid) == 2