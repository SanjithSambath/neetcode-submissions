class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        window_frequency_map = {}
        left = 0
        longest = 0

        for right in range(len(s)):

            char = s[right] # newest character 
            window_frequency_map[char] = window_frequency_map.get(char, 0) + 1 # same as if not in, create + add 1 

            # Keep the most common character; replace all the others.
            while True:
                window_length = right - left + 1
                most_common_count = max(window_frequency_map.values()) # o(1) cuz only 26 letters
                replacements_needed = window_length - most_common_count # majority - extras

                if replacements_needed <= k: # if theres room to continue expanding, break out of this 
                    break

                # if there is too many replacements (greater than K)
                left_char = s[left]
                window_frequency_map[left_char] -= 1 # subtract one from the map
                left += 1 # shrink the window by one

                # only INSIDE this while loop is there a possiblity of window not satisfying k req
                # outsdie the while loop the window alsways can be completed by K
                # so what u do is u seperate the inside and outsdie, insdie is a sandbox where the goal is to get the window shrunk to where it satisfies the K req and the otuside is j adding to it 

            longest = max(longest, right - left + 1) # store only the longest one, either this current window or b4

        return longest