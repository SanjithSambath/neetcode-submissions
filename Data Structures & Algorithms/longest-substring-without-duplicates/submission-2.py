class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = {}

        start_seq = 0
        end_seq = 0
        changing_longest = 0
        actual_longest = 0

        while end_seq < len(s):

            if s[end_seq] not in seen:
                seen[(s[end_seq])] = end_seq
                end_seq += 1
                changing_longest += 1

                if actual_longest < changing_longest:
                    actual_longest = changing_longest
            
            elif s[end_seq] in seen:

                for i in range(seen[s[end_seq]] - start_seq + 1):
                    
                    seen.pop(s[start_seq])
                    changing_longest -= 1
                    start_seq += 1
            
        return actual_longest