class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        seen_s1 = {}
        seen_s2 = {}

        for char in s1:
            if char not in seen_s1:
                seen_s1[char] = 0
            seen_s1[char] += 1

        # built freq map of s1
        

        
        left = 0
        right = 0 

        for i in range(len(s1)):

            right_char = s2[right]

            if right_char not in seen_s2:
                seen_s2[right_char] = 0
                
            seen_s2[right_char] += 1
            
            right += 1
        
        # preload freq map of s2
        print(f"seen s1 {seen_s1}")
        print(f"seen s2 {seen_s2}")
            
        if seen_s1 == seen_s2:
            return True

        right -= 1

        print(f'left = {left} and right = {right}')
        # now slide the window
        while right < (len(s2)-1):

            if seen_s1 == seen_s2:
                return True
            
            right += 1
            print(f'right {right}')

            right_char = s2[right]
            left_char = s2[left]

            if right_char not in seen_s2:
                seen_s2[right_char] = 0
            seen_s2[right_char] += 1

            seen_s2[left_char] -= 1
            if seen_s2[left_char] == 0:
                seen_s2.pop(left_char)

            left += 1
            print(f'seen_s2 = {seen_s2}')
            print(f'seen_s1 = {seen_s1}')

            if seen_s1 == seen_s2:
                return True
        
        return False
