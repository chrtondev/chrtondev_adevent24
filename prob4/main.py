# part 1

file_path = "crossword.txt"

def make_matrix(file_path, num_columns=140):
    # open file
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()] # will read can create lines
        
    if not lines:
        raise ValueError("The file is empty.") # partial input validation
    
    #num_columns = len(lines[0]) # sets # of columns based on the first line
    matrix = []
    
    for line in lines:
        # make sure that each line has same # of columns sent prior
        if len(line) < num_columns:
            row = list(line.ljust(num_columns))
        else:
            row = list(line[:num_columns])
        matrix.append(row)
        
    return matrix

# makes the 2d grid for now word search style approach
matrix = make_matrix(file_path)
'''
# Print the resulting matrix
for row in matrix:
    print(row)
'''

def isValid(x, y, sizeX, sizeY):
    return 0 <= x < sizeX and 0 <= y < sizeY


def findWordInDirection(grid, n, m, word, index, x, y, dirX, dirY):
    # find multiple instances of the word, this method avoids double counting 
    if index == len(word):  # Full word found
        return True

    if isValid(x, y, n, m) and grid[x][y] == word[index]:
        return findWordInDirection(grid, n, m, word, index + 1, x + dirX, y + dirY, dirX, dirY)

    return False

def searchWord(grid, word):
    ans = []
    n = len(grid)
    m = len(grid[0])
    count = 0
    visited = set()

    # directions in word search for 8 possible movements
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for i in range(n):
        for j in range(m):
            if grid[i][j] == word[0]:
                for dirX, dirY in directions:
                    if (i, j, dirX, dirY) not in visited:
                        if findWordInDirection(grid, n, m, word, 0, i, j, dirX, dirY):
                            visited.add((i, j, dirX, dirY))
                            ans.append((i, j))
                            count += 1

    return ans, count


def printResult(ans):
    for a in ans:
       print(f"{{{a[0]},{a[1]}}}", end=" ")
    print()

# will get the answer for part 1
# which is 2603
'''
if __name__ == "__main__":
    word = "XMAS"
    word = word.upper()
    matrix = [[char.upper() for char in row] for row in matrix]
    
    ans, count = searchWord(matrix, word)
    printResult(ans)
    print(f"Total count of '{word}': {count}")
'''


# part two: finding X-MAS

def make_matrix2(file_path, num_columns=140):
    # makes sure that the columns are the correct number as original input when making matrix
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    
    if not lines:
        raise ValueError("The file is empty.")
    
    matrix = []
    for line in lines:
        if len(line) < num_columns:
            row = list(line.ljust(num_columns))
        else:
            row = list(line[:num_columns])
        matrix.append(row)
    
    return matrix

def isValid2(x, y, sizeX, sizeY):
    # make sure cords are in bound
    return 0 <= x < sizeX and 0 <= y < sizeY

def find_xmas_pattern2(grid, x, y):
    # now check for the X-MAS pattern
    n = len(grid)
    m = len(grid[0])
    
    # check on the bounds for the 3x3 pattern
    if not (isValid(x - 1, y - 1, n, m) and isValid(x + 1, y + 1, n, m)):
        return False
    
    # validation for the X-MAS pattern
    diag1 = [grid[x - 1][y - 1], grid[x][y], grid[x + 1][y + 1]]
    diag2 = [grid[x - 1][y + 1], grid[x][y], grid[x + 1][y - 1]]
    
    return (diag1 == ['M', 'A', 'S'] or diag1 == ['S', 'A', 'M']) and \
           (diag2 == ['M', 'A', 'S'] or diag2 == ['S', 'A', 'M'])

def search_xmas2(grid):
    n = len(grid)
    m = len(grid[0])
    count = 0
    
    for x in range(1, n - 1):  # exclude x axis the edges
        for y in range(1, m - 1):  # exclude y axis the edges
            if find_xmas_pattern2(grid, x, y):
                count += 1
    
    return count

if __name__ == "__main__":
    # Example usage
    file_path = "crossword.txt"
    matrix = make_matrix2(file_path)
    
    # Convert all characters to uppercase for consistency
    matrix = [[char.upper() for char in row] for row in matrix]
    
    # Count X-MAS patterns
    xmas_count = search_xmas2(matrix)
    print(f"Total X-MAS patterns found: {xmas_count}")

# above gets the answer for part two finding X-MAS
# re-wrote the functions to better understand them 
# answer = 1965