def calculate_average(list_of_numbers):
    total_sum = 0
    
    for num in list_of_numbers:
        total_sum += num
    
    average = total_sum / len(list_of_numbers)
    
    return average
