class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        d = collections.defaultdict(int)
        for i in range(len(s) - 9):
            cur_str = s[i: i + 10]
            d[cur_str] += 1
            if d[cur_str] == 2:
                ans.append(cur_str)
        return ans