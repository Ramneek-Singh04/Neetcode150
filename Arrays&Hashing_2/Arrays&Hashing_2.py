#Brute Force Solution:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        return s_sorted == t_sorted

# Optimized Solution:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict= {}
        for letter in s:
            if letter in s_dict:
                s_dict[letter] += 1
            else:
                s_dict[letter] = 1
        for letter in t:
            if letter in t_dict:
                t_dict[letter] += 1
            else:
                t_dict[letter] = 1
        return s_dict == t_dict
