# Finding missing numbers in the list
# following the code find support following three scenarios
# 1. it will find the missing number if the list contains duplicates
# 2. if the list contains multiple missing numbers
# 3. if the list contains negative numbers

def finding_missing_number():
    for number_list in number_list_1:
        min_num = min(number_list)
        max_num = max(number_list)
        full_set = set(range(min_num, max_num+1))
        number_list_set = set(number_list)
        missing_number = list(full_set  - number_list_set)
    return missing_number

number_list_1 = [[1,2,4,5], [1,1,1,2,2,2,3,5], [-3,0,1,2,3]]