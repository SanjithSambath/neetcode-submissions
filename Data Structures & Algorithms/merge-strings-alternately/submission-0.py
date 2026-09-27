class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        ptr1 = 0
        ptr2 = 0

        output = ''

        while ptr1 < len(word1) and ptr2 < len(word2):
            output += word1[ptr1]
            output += word2[ptr2]
            
            ptr1 += 1 
            ptr2 += 1
    
        if ptr1 < len(word1):
            output += word1[ptr1:]
        
        if ptr2 < len(word2):
            output += word2[ptr2:]
        
        return output