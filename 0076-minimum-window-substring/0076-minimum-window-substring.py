from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Initialize the dictionaries
        dict_t = defaultdict(int)
        dict_s = defaultdict(int)
        for char in t:
            dict_t[char] += 1

        # Initialize pointers and other variables to track the minimum window
        left, right = 0, 0
        min_len = float('inf')
        min_start = 0
        required_chars = len(dict_t)
        formed_chars = 0

        while right < len(s):
            # Expand the window
            if s[right] in dict_t:
                dict_s[s[right]] += 1
                if dict_s[s[right]] == dict_t[s[right]]:
                    formed_chars += 1

            # Contract the window and move the left pointer to the right
            while left <= right and formed_chars == required_chars:
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    min_start = left

                if s[left] in dict_t:
                    dict_s[s[left]] -= 1
                    if dict_s[s[left]] < dict_t[s[left]]:
                        formed_chars -= 1

                left += 1

            # Move the right pointer to the right
            right += 1

        return "" if min_len == float('inf') else s[min_start:min_start + min_len]
