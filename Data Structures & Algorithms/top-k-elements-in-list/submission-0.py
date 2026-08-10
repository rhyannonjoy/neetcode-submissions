class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # examine inputs: list of integers, integer of frequency
        # examine outputs: most frequent elements within array
        # in any order (doesn't require sorting)

        # question: which elements exist k number of times?

        # constraints
        # list length between 1 - 10^4, never empty
        # index will be beween -1000 and 1000
        # k will be greater than or equal to one
        # checking for bad data? no floats, empty lists

        # initialize frequency map
        frequency_map = {}
        output = []

        # brute force: iterate over nums, add k, v: num, 1 to dictionary
        # search for k value in frequency map, return keys as list

        for num in nums:
            if num in frequency_map.keys():
                frequency_map[num] += 1
            else:
                frequency_map[num] = 1
        
        # Sort dictionary by values in descending order and take top k keys
        sorted_items = sorted(frequency_map.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            output.append(sorted_items[i][0])
            
        return output