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
    sorted_nums = sorted(nums)
    return sorted_nums[0]

def get_max(nums: List[int]) -> int:
    # return max(nums)
    sorted_nums = sorted(nums)
    return sorted_nums[-1]

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
