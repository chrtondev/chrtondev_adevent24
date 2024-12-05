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
    """Find multiple instances of the word, avoiding double-counting overlapping matches."""
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