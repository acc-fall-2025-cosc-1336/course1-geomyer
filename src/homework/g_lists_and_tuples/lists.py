#Homework on Lists and Tuples. get lowest list values no magic methods

def get_lowest_values(input_list, n):
    nums=sorted(input_list)
    lowest_nums=[]
    for i in range(n):
        lowest_nums.append(nums[i])
    return lowest_nums
print(get_lowest_values([8,10,1,50,20],3))


def get_highest_values(input_list, n):
    nums=sorted(input_list, reverse=True)
    highest_nums=[]
    for i in range(n):
        highest_nums.append(nums[i])
    return highest_nums
print(get_highest_values([8,10,1,50,20],2))
