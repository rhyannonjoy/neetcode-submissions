class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # examine inputs: list of strings
        # examine outputs: group anagrams into sublists, list of lists

        # examine constraints/edge cases
        # singletons/empty, return list as is
        # length range 1-10K, strings range 0-100
        # ever get bad data? always lowercase English letters

        # if len(strs) == 1 or not strs:
        #     return strs
        
        # shortcut to anagrams is comparing length of strings
        # sort strings with hash map
        # frequency map because if one string matches the length of
        # another string & also has the same key-value pairs (amount of each letter)
        # then they're an anagram

        # strategy initialize a list (26 letters, a-z), if in list, add to hash map
        # to group strings

        # initialize frequency map
        anagram_grouping = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord("a")] += 1

            anagram_grouping[tuple(count)].append(word)

        return list(anagram_grouping.values())