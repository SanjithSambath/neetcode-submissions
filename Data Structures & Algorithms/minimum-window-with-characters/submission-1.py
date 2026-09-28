class Solution:
    def minWindow(self, s: str, t: str) -> str:

        seen_t = {}
        seen_s = {}

        for char in t:
            if char not in seen_t:
                seen_t[char] = 0
            seen_t[char] += 1

        left = 0

        have = 0
        need = len(seen_t)

        answer_left = 0
        answer_right = 0
        answer_length = float("inf")

        for right in range(len(s)):

            char = s[right]

            if char not in seen_s:
                seen_s[char] = 0

            seen_s[char] += 1

            # did this character JUST become satisfied?
            if char in seen_t and seen_s[char] == seen_t[char]:
                have += 1

            # window contains everything we need
            while have == need:

                current_length = right - left + 1

                if current_length < answer_length:
                    answer_length = current_length
                    answer_left = left
                    answer_right = right

                # try removing left character
                left_char = s[left]
                seen_s[left_char] -= 1

                # did removing it make a requirement unsatisfied?
                if left_char in seen_t and seen_s[left_char] < seen_t[left_char]:
                    have -= 1

                left += 1

        if answer_length == float("inf"):
            return ""

        return s[answer_left:answer_right + 1]