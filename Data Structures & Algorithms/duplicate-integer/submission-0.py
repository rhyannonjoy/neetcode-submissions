class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # input examination: list of integers
        # output examination: return boolean

        # constraints: length will be large, nums can be negative
        # type hinting in definition we're always going to get integers
        # check for bad data?
        # length could be zero or singleton

        if len(nums) == 0 or len(nums) == 1:
            return False
        
        # iterate through nums
        # add to temp set which doesn't allow duplicates
        
        temp_set = set()

        for num in nums:
            if num in temp_set:
                return True
            temp_set.add(num)
        return False
        