class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer = 0
        left_cursor = 0
        used = {}
        
        for right_cursor, char in enumerate(s):
            if char in used and left_cursor <= used[char]: #Duplicated character
                left_cursor = used[char] + 1
            else:
                answer = max(answer, right_cursor - left_cursor + 1)
            used[char] = right_cursor
            
        return answer
