import re
# part 1

file_path = "program.txt"


def compute_cords(coordinates):
    multiplied_cords = []
    for x, y in coordinates:
        result = x * y
        multiplied_cords.append(result)
    
    total = sum(multiplied_cords)
    print(total)


def find_cords(file_path):
    # find all cordinates on line in the txt file (program)
    pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")  # Regex for (x, y)
    coordinates = []
    
    with open(file_path, 'r') as file:
        for line in file:
            # find all matches in the line
            matches = pattern.findall(line)
            for match in matches:
                # clean the match from txt file and split into integers
                x, y = map(int, re.findall(r"\d{1,3}", match))
                coordinates.append((x, y))
    
    
    compute_cords(coordinates)

# will run the two functions to get the answer
# answer = 166630675
# find_cords(file_path)
        

