class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        seen_s1 = {}
        seen_s2 = {}

        for char in s1:
            seen_s1[char] = seen_s1.get(char, 0) + 1

        # Build the first window of s2.
        for right in range(len(s1)):
            right_char = s2[right]
            seen_s2[right_char] = seen_s2.get(right_char, 0) + 1

        if seen_s1 == seen_s2:
            return True

        left = 0

        # Add one character on the right; remove one on the left.
        for right in range(len(s1), len(s2)):
            right_char = s2[right]
            left_char = s2[left]

            seen_s2[right_char] = seen_s2.get(right_char, 0) + 1

            seen_s2[left_char] -= 1
            if seen_s2[left_char] == 0:
                del seen_s2[left_char]

            left += 1

            if seen_s1 == seen_s2:
                return True

        return False