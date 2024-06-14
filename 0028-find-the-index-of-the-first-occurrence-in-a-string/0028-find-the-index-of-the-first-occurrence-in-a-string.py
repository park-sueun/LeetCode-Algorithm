class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        answer = -1
        
        haystack = list(haystack)
        needle = list(needle)
        
        idx = 0
        while idx < len(haystack):
            if haystack[idx] != needle[0]:
                idx += 1
                continue
            
            is_found = True
            for i, v in enumerate(needle):
                if idx + i >= len(haystack):
                    idx += 1
                    is_found = False
                    break
                    
                if haystack[idx + i] != v:
                    idx += 1
                    is_found = False
                    break
                
            if is_found:
                answer = idx
                break
            
        return answer
                