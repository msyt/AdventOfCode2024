# input = ""
# with open(r"C:/Users/soyintu/OneDrive - Manulife/Desktop/notes/exploration/day4_input_trunc.txt", 'r') as fp:
#     for line in fp:   
#         input += line

# fp.close()

def read_grid(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def find_word_in_grid(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),  # Right
        (0, -1),  # Left
        (1, 0),  # Down
        (-1, 0),  # Up
        (1, 1),  # Down-Right
        (1, -1),  # Down-Left
        (-1, 1),  # Up-Right
        (-1, -1)  # Up-Left
    ]
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def search_from(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True
    
    count = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if search_from(x, y, dx, dy):
                    count += 1
    return count

# Read the grid from the file
file_path = r"day4_input.txt"
grid = read_grid(file_path)

# Find and count the occurrences of the word "XMAS"
word = "XMAS"
count = find_word_in_grid(grid, word)

print(f"The word '{word}' appears {count} times in the grid.")
