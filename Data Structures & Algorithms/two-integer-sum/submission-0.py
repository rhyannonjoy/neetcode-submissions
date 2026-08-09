class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # examine input: list of integters `nums` with integer `target`
        # examine output: list of integers
        # return indices that add up to target
        # return smaller indices first
        # i cannot be equal to j

        # examine constraints
        # nums length btwn 2-1K
        # values range -10m and 10m
        # target range -10m and 10m

        # edge cases, test cases
        # do we need to check for an empty nums?
        # constraints cite length at least 2
        # do we need to sanitize for negative/floats
        # only args integers, including negs

        # strategy
        # brute force would be iterating over nums
        # build a map with key: integer, value: integer's index

        # initialize map
        int_index_map = {}
        
        # the length of nums, keep track of index
        for index, current_number in enumerate(nums):
            difference = target - current_number
            if difference in int_index_map:
                return [int_index_map[difference], index]
            int_index_map[current_number] = index
        return
                