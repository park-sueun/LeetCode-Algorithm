class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        strs = sorted(strs)
        
        result = None
        first, last = strs[0], strs[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            result = i
        return "".join(first[:result+1]) if result is not None else ""