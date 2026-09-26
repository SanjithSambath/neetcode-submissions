class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for word in strs: 

            for i in range(len(prefix)):

                if prefix in word[:len(prefix)]:
                    break
                    
                prefix = prefix[:-1]

        return prefix
        