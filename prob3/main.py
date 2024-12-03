import re
# part 1

file_path = "cleaned_program.txt"


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
find_cords(file_path)
        

# PART two


# i need to visualize the do()'s and don't()'s
def print_colorized_text(file_path):
    """
    Print the contents of the file with do() in green and don't() in red.
    """
    # Regex to match do() and don't()
    pattern = re.compile(r"do\(\)|don't\(\)")
    
    with open(file_path, 'r') as file:
        for line in file:
            # Replace do() with green and don't() with red
            colorized_line = pattern.sub(
                lambda match: (
                    f"\033[32m{match.group(0)}\033[0m"  # Green for do()
                    if match.group(0) == "do()" else
                    f"\033[31m{match.group(0)}\033[0m"  # Red for don't()
                ),
                line
            )
            print(colorized_line, end='')  # Print the colorized line
# this color check works          
# print_colorized_text(file_path)

# i will remove the text after don't()s
def clean_program(file_path, output_path="cleaned_program.txt"):
    """
    Cleans the program by removing text between `don't()` and `do()` instructions.
    Saves the cleaned text to a new file.
    """
    with open(file_path, 'r') as file:
        text = file.read()

    # Regex to locate `do()` and `don't()`
    instructions_pattern = re.compile(r"(do\(\)|don't\(\))")
    matches = list(instructions_pattern.finditer(text))
    
    cleaned_text = ""
    enabled = True  # Default state is enabled
    last_valid_index = 0

    for match in matches:
        instruction = match.group(0)
        position = match.start()

        if instruction == "don't()":
            if enabled:
                # Append valid text up to this point
                cleaned_text += text[last_valid_index:position]
                enabled = False  # Disable future text processing
        elif instruction == "do()":
            if not enabled:
                # Re-enable processing and mark the valid start index
                last_valid_index = match.end()
                enabled = True

    # Append remaining valid text after the last `do()` (if enabled)
    if enabled:
        cleaned_text += text[last_valid_index:]

    # Save cleaned text to a new file
    with open(output_path, 'w') as output_file:
        output_file.write(cleaned_text)

    print(f"Cleaned program saved to {output_path}")
    
# clean_program(file_path, output_path="cleaned_program.txt")