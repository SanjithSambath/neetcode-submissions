class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}
        left = 0
        longest = 0

        for right in range(len(s)):
            # Include the new character in the window.
            char = s[right]
            frequency[char] = frequency.get(char, 0) + 1

            # Keep the most common character; replace all the others.
            while True:
                window_length = right - left + 1
                most_common_count = max(frequency.values())
                replacements_needed = window_length - most_common_count

                if replacements_needed <= k:
                    break

                # Too many replacements: remove the leftmost character.
                left_char = s[left]
                frequency[left_char] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest