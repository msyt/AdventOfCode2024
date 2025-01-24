def read_grid(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def count_x_mas_patterns(grid):
    T = list('MAS'), list('SAM')
    
    # Assuming grid is a 2D list and has at least 3x3 size
    rows = len(grid)
    cols = len(grid[0])
    
    # Prepare valid center positions
    g = [(i, j) for i in range(1, rows - 1) for j in range(1, cols - 1)]
    
    # Count occurrences of the pattern
    return sum([grid[i + d][j + d] for d in (-1, 0, 1)] in T and
               [grid[i + d][j - d] for d in (-1, 0, 1)] in T for i, j in g)

# Example usage
file_path = r"day4_input.txt"
grid = read_grid(file_path)  # Assuming read_grid function is defined as before
count = count_x_mas_patterns(grid)

print(f"The 'X-MAS' pattern appears {count} times in the grid.")