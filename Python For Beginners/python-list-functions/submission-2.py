from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    # return sum(nums)
    count = 0
    for num in nums:
        count += num
    return count

def get_min(nums: List[int]) -> int:
    # return min(nums)
    
    # use sorted method, return[0]
    # sorted_nums = sorted(nums)
    # return sorted_nums[0]

    # use for loop with comparison
    current_min = nums[0]
    for num in nums:
        if num < current_min:
            current_min = num
    return current_min

def get_max(nums: List[int]) -> int:
    # return max(nums)
    
    # use sorted method
    # sorted_nums = sorted(nums)
    # return sorted_nums[-1]

    # use for loop with comparison
    current_max = nums[0]
    for num in nums:
        if num > current_max:
            current_max = num
    return current_max

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
