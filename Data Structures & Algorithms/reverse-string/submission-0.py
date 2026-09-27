class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        ptr = 0
        while ptr < len(s):
            s.insert(ptr, s[-1])
            s.pop()
            ptr += 1