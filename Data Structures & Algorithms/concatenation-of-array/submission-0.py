class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # nums = list(len(n))
        # ans is the concatenation of 2 nums arrays, return ans
        # create an array named ans = len(2n)
        # conditional statements
        # ans[i] == nums[i]
        # ans[i + n] == nums [i]
        # for 0 <= i < n (0-indexed)

        # test cases / edge cases / constraints
        # bad data? no sanitation of data required
        # we're not going to get negative numbers
        # we're always going to get integers
        # parameters list of integers, return a list of integers
        # we have ranges described, type hints, no step defined
        # nums will always be populated, even if its a singleton
        # think about de-duplication when the problem is essentially
        # duplicating an array

        # strategy
        # iterate through nums
        # append each i to ans
        # only do this twice

        first_ans = list()
        second_ans = list()
        for i in nums:
            first_ans.append(i)
            second_ans.append(i)
        
        return first_ans + second_ans

        # Time space complexity - O(n)? Because O(n + n)
        # This can be made more efficient using only 1 data structure

        ans = []
        for i in range(2):
            for nums in nums:
                ans.append(nums)
        return ans
