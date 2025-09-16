class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_table = {}

        for string in strs:
            sorted_string = ''.join(sorted(string))

            if sorted_string not in strs_table:
                strs_table[sorted_string] = []

            strs_table[sorted_string].append(string)

        return list(strs_table.values())

#62.68% Beats

class Solution: #82.60%
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted not in anagrams:
                anagrams[s_sorted] = []
            anagrams[s_sorted].append(s)
            
        return [list(value) for key, value in anagrams.items()]

"""
Time: O(n · k log k)
Space: O(n · k)
"""
