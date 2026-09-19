class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        final_groups = {}

        for word in strs:
            freq_list = [0] * 26 # init

            for letter in word: 
                
                freq_index = ord(letter) - ord('a') # gives normalized ord
                freq_list[freq_index] += 1
            
            key = tuple(freq_list)

            if key not in final_groups:
                final_groups[key] = []

            final_groups[key].append(word)

        return list(final_groups.values())
        
        