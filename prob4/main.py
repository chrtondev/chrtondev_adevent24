# part 1

file_path = "crossword.txt"

def make_matrix(file_path):
    # open file
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()] # will read can create lines
        
    if not lines:
        raise ValueError("The file is empty.") # partial input validation
    
    num_columns = len(lines[0]) # sets # of columns based on the first line
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

# Print the resulting matrix
#for row in matrix:
#    print(row)

