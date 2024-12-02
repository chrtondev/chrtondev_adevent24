# PART 1
file_path = "levels.txt"

def lst_validate(lst):
    # validation to check in asc or desc by min 1 at most 3
    is_ascending = all(1 <= lst[i + 1] - lst[i] <= 3 for i in range(len(lst) - 1))
    is_descending = all(1 <= lst[i] - lst[i + 1] <= 3 for i in range(len(lst) - 1))
    return is_ascending or is_descending  # will be valid if either condition is true


def check_safe(file_path, max_lines=1000):
    valid_count = 0
    # begin parse
    with open(file_path, 'r') as file:
        for line_num, line in enumerate(file, start=1):
            if line_num > max_lines:
                break  # to stop processing after max_lines lines
            
            # convert the line to a list of integers
            lst = list(map(int, line.strip().split()))
            
            # use the validation function 
            lst = list(map(int, line.strip().split()))
            
            # validate the line converted to list "levels"
            is_valid = lst_validate(lst)
            if is_valid:
                valid_count += 1  # incrementer
            
    
    # Print total count of valid lines
    print(f"Total Valid Lines: {valid_count}")


# run function for part 1
# answer = 359
# check_safe(file_path, max_lines=1000)