class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # examine inputs: parameters 2 strings
        # examine outputs: return a Boolean

        # examine constraints
        # check for bad data? no
        # always get lowercase English letters

        # edge cases or singletons

        # if length differs then no anagram
        if len(s) != len(t):
            return False
        
        # build a dictionary
        # assigns key is the letter, value is how many
        # compare dictionaries?
        
        # iterate through each string
        # check if each letter in s exists in t

        # initialize two dictionaries
        s_dictionary = dict()
        t_dictionary = dict()

        # populate two dictionaries
        for i in range(len(s)):
            s_dictionary[s[i]] = 1 + s_dictionary.get(s[i], 0)
            t_dictionary[t[i]] = 1 + t_dictionary.get(t[i], 0)
        # check lengths
        for letter in s_dictionary:
            if s_dictionary[letter] != t_dictionary.get(letter, 0):
                return False
        
        return True
