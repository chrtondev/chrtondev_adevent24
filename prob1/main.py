
def process_numbers(file_path):
    list1 = []
    list2 = []
    with open(file_path, 'r') as file:
        for line in file:
            # split line by the tab spacing two get both numbers
            num1, num2 = map(int, line.strip().split())
            list1.append(num1)
            list2.append(num2)
            
    def add_commas(lst):
        # add commas so the list is funcitonal
        return ', '.join(map(str, lst))
            

    
    return list1, list2



file_path = "numbers.txt"
list1, list2= process_numbers(file_path)

final_list1 = sorted(list1)
final_list2 = sorted(list2)

def calculate_distance():
    total_distance = []
    for num1, num2 in zip(final_list1, final_list2):
        distance = int(num2) - int(num1)
        if (distance < 0):
            distance = int(distance) * -1
            total_distance.append(distance)
        else:
            total_distance.append(distance)
    
    print(sum(total_distance))

# Provides the answer to part 1 = 2375403
# calculate_distance()
            
# part 2
list1, list2= process_numbers(file_path)

def claculate_sim_score(first_list, second_list):
    occurnces = []
    for num1, num2 in zip(first_list, second_list):
        num_occurnces = second_list.count(num1)
        sim_score = int(num1) * int(num_occurnces)
        occurnces.append(sim_score)
        
    print(sum(occurnces))
    
# Provides answer to part 2 = 2308227
# claculate_sim_score(list1, list2)